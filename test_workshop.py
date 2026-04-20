#!/usr/bin/env python3
"""
Workshop Test Script - Verify everything works
"""
import sys

def test_imports():
    """Test all imports work"""
    print("🧪 Testing imports...")
    try:
        from strands import Agent, tool
        from strands.models import BedrockModel
        import streamlit
        import boto3
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_tools():
    """Test tool creation"""
    print("\n🧪 Testing tool decorator...")
    try:
        from tools.flight_tools import search_flights
        from tools.hotel_tools import find_hotels
        from tools.weather_tools import get_weather
        print("✅ All tools loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Tool loading failed: {e}")
        return False

def test_agents():
    """Test agent creation"""
    print("\n🧪 Testing agents...")
    try:
        from agents.flight_agent import create_flight_agent
        from agents.hotel_agent import create_hotel_agent
        from agents.itinerary_agent import create_itinerary_agent
        from agents.destination_agent import create_destination_agent
        print("✅ All agents loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Agent loading failed: {e}")
        return False

def test_orchestrator():
    """Test orchestrator"""
    print("\n🧪 Testing orchestrator...")
    try:
        from orchestrator import create_orchestrator
        orchestrator = create_orchestrator()
        print(f"✅ Orchestrator created: {orchestrator.name}")
        return True
    except Exception as e:
        print(f"❌ Orchestrator failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("AWS STRANDS WORKSHOP - SYSTEM TEST")
    print("=" * 60)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Tools", test_tools()))
    results.append(("Agents", test_agents()))
    results.append(("Orchestrator", test_orchestrator()))
    
    print("\n" + "=" * 60)
    print("TEST RESULTS")
    print("=" * 60)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name:20s}: {status}")
    
    all_pass = all(r for _, r in results)
    
    print("\n" + "=" * 60)
    if all_pass:
        print("🎉 ALL TESTS PASSED - Workshop is ready!")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Run: streamlit run app.py")
        print("2. Open browser at http://localhost:8501")
        print("3. Start building your agent!")
        return 0
    else:
        print("⚠️  SOME TESTS FAILED - Check errors above")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
