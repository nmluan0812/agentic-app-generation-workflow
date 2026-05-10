#!/usr/bin/env python3
"""
Test script to run the agentic app generation workflow
"""

import asyncio
import sys
import os

# Add the orchestrator directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'orchestrator'))

from main import OrchestratorAgent, WorkflowConfig

async def test_workflow():
    """Test the complete workflow with a sample app description"""
    
    # Create configuration (simulation mode to avoid API calls)
    config = WorkflowConfig(
        lovable_api_key="test-key",
        vercel_token="test-token",
        github_token="test-token",
        stripe_api_key="test-key",
        simulation_mode=True,  # Important: Use simulation mode to avoid rate limits
        update_interval=5  # Shorter interval for testing
    )
    
    # Create orchestrator agent
    agent = OrchestratorAgent(config)
    
    # Test app description
    app_description = """
    Create a task management application where users can:
    - Create, read, update, and delete tasks
    - Mark tasks as complete/incomplete
    - Organize tasks into projects
    - Set due dates and reminders
    - Collaborate with team members
    - Track progress with analytics dashboard
    """
    
    print("Starting test workflow execution...")
    print("=" * 50)
    
    # Run the workflow
    result = await agent.run_workflow(app_description)
    
    print("=" * 50)
    print("Workflow execution completed!")
    print(f"Status: {result['status']}")
    
    if result['status'] == 'success':
        print(f"Preview URL: {result.get('preview_url', 'N/A')}")
        print(f"Deployment info available: {'deployment_info' in result}")
        print(f"Workflow data keys: {list(result.get('workflow_data', {}).keys())}")
    else:
        print(f"Error: {result.get('error', 'Unknown error')}")
        print(f"Failed at stage: {result.get('stage', 'Unknown')}")
    
    return result

if __name__ == "__main__":
    # Run the test
    result = asyncio.run(test_workflow())
    
    # Exit with appropriate code
    sys.exit(0 if result['status'] == 'success' else 1)