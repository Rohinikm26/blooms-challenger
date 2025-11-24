import os
import streamlit as st
import json
import time
from typing import List, Dict
from google import genai
from google.genai import types
from dotenv import load_dotenv

# --- SETUP ---
# Load environment variables (API Key)
load_dotenv()

# Check for API Key
if "GOOGLE_API_KEY" not in os.environ:
    print("❌ ERROR: GOOGLE_API_KEY not found. Please set it in your .env file or terminal.")
    exit()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
MODEL_ID = "gemini-flash-latest"  # Using 1.5 Flash for better free-tier stability

# --- FEATURE 1: CUSTOM TOOL (The Pruner) ---
def tool_fallacy_check(argument_text: str) -> str:
    """
    Analyzes text for logical fallacies to help the Challenger 'prune' bad ideas.
    """
    print(f"\n[TOOL] 🍂 Scanning for dead branches (fallacies) in: '{argument_text[:30]}...'")
    
    prompt = f"""
    Analyze the following argument for logical fallacies.
    Argument: "{argument_text}"
    Return ONLY a raw JSON object: {{ "found": boolean, "fallacies": [list of strings], "critique": "short explanation" }}
    """
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )
        return response.text
    except Exception as e:
        return json.dumps({"found": False, "error": str(e)})

# --- FEATURE 2: SESSION MANAGEMENT ---
class DebateSession:
    def __init__(self, topic):
        self.topic = topic
        self.history: List[Dict] = []
        self.round_count = 0
        self.status = "ACTIVE"
    
    def add_event(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_history_text(self):
        return "\n".join([f"{item['role'].upper()}: {item['content']}" for item in self.history])

# --- FEATURE 3: THE AGENTS ---

def agent_challenger(session: DebateSession, last_user_input: str):
    """
    Agent 1: Bloom's Challenger.
    Uses the tool to find flaws, then pushes the user to higher cognitive levels.
    """
    print("\n🌻 Bloom's Challenger is analyzing root structure...")
    
    # 1. Run Tool (With Retry/Sleep for safety)
    time.sleep(2) 
    try:
        tool_result = tool_fallacy_check(last_user_input)
        tool_data = json.loads(tool_result)
    except:
        tool_data = {"found": False}
    
    # 2. Build Context
    fallacy_note = ""
    if tool_data.get("found"):
        fallacy_note = f"OBSERVATION: The user's idea has dead branches (fallacies): {tool_data['fallacies']}. Prune these gently."
        print(f"   -> ⚠️  Detected: {', '.join(tool_data['fallacies'])}")

    prompt = f"""
    You are 'Bloom's Challenger'. 
    Your Goal: Use Bloom's Taxonomy to push the user to higher levels of thinking.
    
    - Do not just argue. Ask probing questions that force Analysis and Evaluation.
    - If their logic is weak, act as a "Gardener" pruning dead leaves (exposing flaws).
    - If their logic is strong, push them to the "Create" level (ask how they would implement this).
    
    HISTORY:
    {session.get_history_text()}
    
    CURRENT INPUT: "{last_user_input}"
    {fallacy_note}
    
    TASK:
    Respond to the user. Be encouraging but intellectually demanding. 
    Use gardening metaphors occasionally. Keep it under 3 sentences.
    """
    
    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        content = response.text
        session.add_event("challenger", content)
        return content
    except Exception as e:
        return f"Error: {str(e)}"

def agent_evaluator(session: DebateSession):
    """
    Agent 2: The Evaluator.
    Checks if the user has demonstrated growth/strength for 3 rounds.
    """
    print("\n⚖️  Evaluator is measuring growth...")
    
    if session.round_count < 3:
        return "CONTINUE"

    prompt = f"""
    You are a Debate Evaluator checking for "Intellectual Growth".
    
    DEBATE LOG: 
    {session.get_history_text()}
    
    RULES:
    1. If the user has merely repeated themselves, return "LOSE".
    2. If the user has conceded key points without defending the core idea, return "LOSE".
    3. If the user has demonstrated "Higher Order Thinking" (Analysis/Evaluation) for 3 rounds, return "WIN".
    
    OUTPUT FORMAT:
    Return ONLY one word: "WIN", "LOSE", or "CONTINUE".
    """
    
    time.sleep(2)
    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text.strip()
    except:
        return "CONTINUE"

# --- MAIN LOOP ---

def run_blooms_garden():
    print("--- 🌻 WELCOME TO BLOOM'S GARDEN ---")
    print("--- Let's grow your ideas through rigorous challenge ---")
    
    topic = input("\n🌱 Plant your idea (Enter a topic): ")
    session = DebateSession(topic)
    
    print(f"\n[SYSTEM] Garden initialized. Topic: {topic}")
    
    while session.status == "ACTIVE":
        # 1. User Turn
        user_input = input("\n🗣️  You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("👋 Leaving the garden.")
            break
            
        session.add_event("user", user_input)
        
        # 2. Challenger Turn
        challenger_reply = agent_challenger(session, user_input)
        print(f"\n🌻 Challenger: {challenger_reply}")
        
        # 3. Evaluator Turn
        verdict = agent_evaluator(session)
        
        # 4. Loop Logic
        if "WIN" in verdict:
            print("\n🌳 FULLY GROWN! You have mastered this topic.")
            session.status = "WIN"
        elif "LOSE" in verdict:
            print("\n🥀 WITHERED. Your argument could not sustain growth.")
            session.status = "LOSE"
        else:
            session.round_count += 1
            print(f"--- Growth Stage {session.round_count} Complete ---\n")

if __name__ == "__main__":
    run_blooms_garden()