"""
UX Conversation Module

Stateful conversational interface with context memory and guidance.

TODO: Integrate with NLP models for better conversation understanding.
"""

from feedback_user_interaction import ConversationalInterface


class StatefulConversationalInterface:
    """Conversational interface with memory and guidance."""
    
    def __init__(self):
        self.base_interface = ConversationalInterface()
        self.memory = []  # conversation history
    
    def interact(self, user_input):
        """
        Process user input and store in history.
        
        Args:
            user_input: User's message/query
            
        Returns:
            str: Acknowledgment message
        """
        # Store in memory
        self.memory.append({
            "type": "user",
            "content": user_input,
            "timestamp": self._get_timestamp()
        })
        
        # Get response from base interface
        response = self.base_interface.interact(user_input)
        
        # Store response in memory
        self.memory.append({
            "type": "system",
            "content": response,
            "timestamp": self._get_timestamp()
        })
        
        return response
    
    def guide_next_steps(self, context):
        """
        Provide guidance on next steps based on context.
        
        Args:
            context: dict with current system state/context
            
        Returns:
            list[str]: Suggested next steps
        """
        suggestions = []
        
        # Analyze context and provide suggestions
        if context.get("risks"):
            suggestions.append("Review and mitigate identified risks")
        
        if context.get("conflicts"):
            suggestions.append("Resolve requirement conflicts")
        
        if context.get("compliance"):
            violations = context.get("compliance", [])
            if violations:
                suggestions.append(f"Address {len(violations)} compliance violation(s)")
        
        # Generic suggestions if no specific issues
        if not suggestions:
            suggestions.extend([
                "Continue iterating on design",
                "Run additional simulations",
                "Gather stakeholder feedback"
            ])
        
        return suggestions
    
    def get_history(self):
        """
        Get conversation history.
        
        Returns:
            list[dict]: Conversation history
        """
        return self.memory
    
    def _get_timestamp(self):
        """Get current timestamp."""
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat()
