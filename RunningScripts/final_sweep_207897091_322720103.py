import wandb
YOUR_WANDB_USERNAME = "noa-levi"
project = "NLP2024_PROJECT_207897091_322720103"

command = [
        "${ENVIRONMENT_VARIABLE}",
        "${interpreter}",
        "StrategyTransfer.py",
        "${project}",
        "${args}"
    ]

sweep_config_1 = {
    "name": "decide between relaxed strategies",
    "method": "grid",
    "metric": {
        "goal": "maximize",
        "name": "AUC.test.max"
    },
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [17,18,19,20,21,22,23,24]},
    },
    "command": command
}
sweep_config_1_no_metric = {
    "name": "decide between relaxed strategies",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [17,18,19,20,21,22,23,24]},
    },
    "command": command
}
sweep_config_2_no_metric = {
    "name": "decide between unrelaxed first and last new astrengies",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [25,26,27,28]},
    },
    "command": command
}

sweep_config_3_with_metric_all = {
    "name": "decide between all new astrengies with metric",
    "method": "grid",
    "metric": {
        "goal": "maximize",
        "name": "AUC.test.max"
    },
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [17,18,19,20,21,22,23,24,25,26,27,28]},
    },
    "command": command
}
sweep_config_only_new_no_metric = {
    "name": "decide between only new astrengies. no mettric_just ef",
    "method": "grid",
    # "metric": {
    #     "goal": "maximize",
    #     "name": "AUC.test.max"
    # },
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "architecture": {"values": ["LSTM"]},
        "online_simulation_factor": {"values": [0, 4]},
        # "features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [25,26,27,28]},
    },
    "command": command
}
sweep_config_3_no_metric_all = {
    "name": "decide between all new astrengies with no metric",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [17,18,19,20,21,22,23,24,25,26,27,28]},
    },
    "command": command
}
sweep_config_eilam_change = {
    "name": "run eilam basic with changes on sweep config",
    "method": "grid",
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        # "features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [12]},
    },
    "command": command
}
# sweep_config_0 = {
#     "name": "initialize",
#     "method": "grid",
#     "parameters": {
#         "ENV_HPT_mode": {"values": [True]},
#         "seed": {"values": list(range(1, 6))},
#         "basic_nature": {"values": [17,18,19,20,21,22,23,24]},
#     },
#     "command": command
# }
# sweep_config = {
#     "name": "TRYING TO FIX THE BUGS",
#     "method": "grid",
#     "metric": {
#         "goal": "maximize",
#         "name": "AUC.test.max"
#     },
#     "parameters": {
#         "ENV_HPT_mode": {"values": [False]},
#         "seed": {"values": list(range(1, 6))},
#     },
#     "command": command
# }

# sweep_config_00 = {
#     "name": "TRYING TO FIX THE BUGS",
#     "method": "grid",
#     "parameters": {
#         "ENV_HPT_mode": {"values": [True]},
#         "seed": {"values": list(range(1, 6))},
#     },
#     "command": command
# }

sweep_config = {
    "name": "run eilam basic sweep config",
    "method": "grid",
    "metric": {
        "goal": "maximize",
        "name": "AUC.test.max"
    },
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        "features": {"values": ["EFs", "GPT4", "BERT"]},
    },
    "command": command
}

sweep_config_true = {
    "name": "run eilam basic sweep config WITH TRUE",
    "method": "grid",
    "metric": {
        "goal": "maximize",
        "name": "AUC.test.max"
    },
    "parameters": {
        "ENV_HPT_mode": {"values": [True]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        "features": {"values": ["EFs", "GPT4", "BERT"]},
    },
    "command": command
}

sweep_config_final = {
    "name": "run final config on best astrategies on test set",
    "method": "grid",
    # "metric": {
    #     "goal": "maximize",
    #     "name": "AUC.test.max"
    # },
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        #"architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [24,25,27,26,28, 12]},
    },
    "command": command
}
sweep_config_final_other_combinations = {
    "name": "run final config_other comb",
    "method": "grid",
    # "metric": {
    #     "goal": "maximize",
    #     "name": "AUC.test.max"
    # },
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        #"architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [0, 4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [29,20,31,32,33]},
    },
    "command": command
}
sweep_config_final_try_to_complete = {
    "name": "try to complete - 32, 33,27,26,28,12",
    "method": "grid",
    # "metric": {
    #     "goal": "maximize",
    #     "name": "AUC.test.max"
    # },
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        #"architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [32, 33,27,26,28,12]},
    },
    "command": command
}

sweep_config_final_try_to_complete_2 = {
    "name": "try to complete -21, 30, 34",
    "method": "grid",
    # "metric": {
    #     "goal": "maximize",
    #     "name": "AUC.test.max"
    # },
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "architecture": {"values": ["LSTM"]},
        "seed": {"values": list(range(1, 6))},
        "online_simulation_factor": {"values": [4]},
        #"features": {"values": ["EFs", "GPT4", "BERT"]},
        "basic_nature": {"values": [21, 30, 34]},
    },
    "command": command
}


# sweep_id = wandb.sweep(sweep=sweep_config, project=project)
# print("run this line to run your agent in a screen:")
# print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")

sweep_id = wandb.sweep(sweep=sweep_config_final_try_to_complete_2, project=project)
print("run this line to run your agent in a screen:")
print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")
# sweep_id = wandb.sweep(sweep=sweep_config_0, project=project)
# print("run this line to run your agent in a screen:")
# print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")
