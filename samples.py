beans_tokens = {
    "rule_type_data": {
        "uid": "rule:liana:new_beans_card",
        "title": "Register",
        "statement": "Join our rewards program and get x points",
        "is_active": True,
        "settings": {
            "drcr": {
                "type": "choice",
                "label": "Transaction type",
                "hidden": True,
                "choices": ["credit", "credit"],
                "default": "credit",
                "help_text": "Whether this rule triggers a credit or debit transaction.",
            },
            "beans": {
                "type": "integer",
                "label": "Points",
                "default": 300,
                "help_text": "The number of points to award to shoppers when they complete the action.",
            },
            "title": {
                "type": "text",
                "label": "Title",
                "default": "Register",
                "help_text": "Rule title (used for translation)",
            },
            "statement": {
                "type": "text",
                "label": "Statement",
                "default": "Join our rewards program and get [beans]",
                "help_text": "A statement describing the rule to shoppers.",
            },
            "help_text": {
                "type": "text",
                "label": "Help Text",
                "default": "Join now to receive your credit",
                "help_text": "Let customers know how to perform the action to earn points",
            },
            "position": {
                "type": "integer",
                "label": "Position",
                "default": 1,
                "help_text": "The position of the rule when listing the rules on the rewards program page.",
            },
        },
    },
    "new_rule_type_data": {
        "title": "Loyalty",
        "statement": "Get x points for each FCFA (USD) spent in our online shop",
        "is_active": True,
        "settings": {
            "drcr": {
                "type": "choice",
                "label": "Transaction type",
                "hidden": True,
                "choices": ["credit", "credit"],
                "default": "credit",
                "help_text": "Whether this rule triggers a credit or debit transaction.",
            },
            "beans": {
                "type": "integer",
                "label": "Points",
                "default": 10,
                "help_text": "The number of points to award to shoppers when they complete the action.",
            },
            "title": {
                "type": "text",
                "label": "Title",
                "default": "Register",
                "help_text": "Rule title (used for translation)",
            },
            "statement": {
                "type": "text",
                "label": "Statement",
                "default": "Join our rewards program and get [beans]",
                "help_text": "A statement describing the rule to shoppers.",
            },
            "help_text": {
                "type": "text",
                "label": "Help Text",
                "default": "Join now to receive your credit",
                "help_text": "Let customers know how to perform the action to earn points",
            },
            "position": {
                "type": "integer",
                "label": "Position",
                "default": 1,
                "help_text": "The position of the rule when listing the rules on the rewards program page.",
            },
        },
    },
}
