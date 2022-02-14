""" =================================================
# Copyright (c) Facebook, Inc. and its affiliates
Authors  :: Vikash Kumar (vikashplus@gmail.com), Vittorio Caggiano (caggiano@gmail.com)
================================================= """

from gym.envs.registration import register
import os
import numpy as np

curr_dir = os.path.dirname(os.path.abspath(__file__))

print("RS:> Registering Myo Envs")

# Finger-tip reaching ==============================
register(id='motorFingerReachFixed-v0',
        entry_point='mj_envs.envs.myo.reach_v0:ReachEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_motorAct_v0.xml',
            'target_reach_range': {'IFtip': ((0.2, 0.05, 0.20), (0.2, 0.05, 0.20)),},
            'normalize_act': True,
            'frame_skip': 5,
        }
    )
register(id='motorFingerReachRandom-v0',
        entry_point='mj_envs.envs.myo.reach_v0:ReachEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_motorAct_v0.xml',
            'target_reach_range': {'IFtip': ((0.27, .1, .3), (.1, -.1, .1)),},
            'normalize_act': True,
            'frame_skip': 5,
        }
    )
register(id='myoFingerReachFixed-v0',
        entry_point='mj_envs.envs.myo.reach_v0:ReachEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_muscleAct_v0.xml',
            'target_reach_range': {'IFtip': ((0.2, 0.05, 0.20), (0.2, 0.05, 0.20)),},
            'normalize_act': True,
        }
    )

register(id='myoFingerReachRandom-v0',
        entry_point='mj_envs.envs.myo.reach_v0:ReachEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_muscleAct_v0.xml',
            'target_reach_range': {'IFtip': ((0.27, .1, .3), (.1, -.1, .1)),},
            'normalize_act': True,
        }
    )

# Elbow posing ==============================
register(id='myoElbowPose1D1MRandom-v0', # remove
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof1muscle.xml',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random'
        }
    )

register(id='myoElbowPose1D6MFixed-v0',
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles.xml',
            'target_jnt_range': {'r_elbow_flex':(2, 2),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random'
        }
    )
register(id='myoElbowPose1D6MRandom-v0',
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles.xml',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random'
        }
    )

register(id='myoElbowPose1D6MExoFixeds-v0',
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles_1dofexo.xml',
            'target_jnt_range': {'r_elbow_flex':(2, 2),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random',
            'weighted_reward_keys':{
                                "pose": 1.0,
                                "bonus": 4.0,
                                "act_reg": 5.0,
                                "penalty": 50,
            }
        }
    )
register(id='myoElbowPose1D6MExoRandom-v0',
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles_1dofexo.xml',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random',
            'weight_bodyname':'carry_weight',
            'weight_range':(.1, 2),
            'weighted_reward_keys':{
                                "pose": 1.0,
                                "bonus": 4.0,
                                "act_reg": 5.0,
                                "penalty": 50,
            }
        }
    )


register(id='myoElbowPose1D6M_SoftExo_Random-v0', # Kill
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/arm/elbow_1dof6muscles_1dofsoftexo.xml',
            'target_jnt_range': {'r_elbow_flex':(0, 2.27),},
            'viz_site_targets': ('wrist',),
            'normalize_act': True,
            'pose_thd': .175,
            'reset_type': 'random',
            'weighted_reward_keys':{
                                "pose": 1.0,
                                "bonus": 4.0,
                                "act_reg": 5.0,
                                "penalty": 50,
            }
        }
    )

# Finger-Joint posing ==============================
register(id='motorFingerPoseFixed-v0',
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_motorAct_v0.xml',
            'target_jnt_range': {'IFadb':(0, 0),
                                'IFmcp':(0, 0),
                                'IFpip':(.75, .75),
                                'IFdip':(.75, .75)
                                },
            'viz_site_targets': ('IFtip',),
            'normalize_act': True,
            'frame_skip': 5,
        }
)
register(id='motorFingerPoseRandom-v0',
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_motorAct_v0.xml',
            'target_jnt_range': {'IFadb':(-.2, .2),
                                'IFmcp':(-.4, 1),
                                'IFpip':(.1, 1),
                                'IFdip':(.1, 1)
                                },
            'viz_site_targets': ('IFtip',),
            'normalize_act': True,
            'frame_skip': 5,
        }
    )
register(id='myoFingerPoseFixed-v0',
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_muscleAct_v0.xml',
            'target_jnt_range': {'IFadb':(0, 0),
                                'IFmcp':(0, 0),
                                'IFpip':(.75, .75),
                                'IFdip':(.75, .75)
                                },
            'viz_site_targets': ('IFtip',),
            'normalize_act': True,
        }
    )
register(id='myoFingerPoseRandom-v0',
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/finger/tendon_finger_muscleAct_v0.xml',
            'target_jnt_range': {'IFadb':(-.2, .2),
                                'IFmcp':(-.4, 1),
                                'IFpip':(.1, 1),
                                'IFdip':(.1, 1)
                                },
            'viz_site_targets': ('IFtip',),
            'normalize_act': True,
        }
    )

# Hand-Joint posing ==============================

# Remove this when the ASL envs stablizes
register(id='myoHandPoseFixed-v0', #kill
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_pose.xml',
            'viz_site_targets': ('THtip','IFtip','MFtip','RFtip','LFtip'),
            'target_jnt_value': np.array([0, 0, 0, -0.0904, 0.0824475, -0.681555, -0.514888, 0, -0.013964, -0.0458132, 0, 0.67553, -0.020944, 0.76979, 0.65982, 0, 0, 0, 0, 0.479155, -0.099484, 0.95831, 0]),
            'normalize_act': True,
            'pose_thd': .7,
            'reset_type': "init",        # none, init, random
            'target_type': 'fixed',      # switch / generate/ fixed
        }
    )

# Create ASL envs ==============================
jnt_namesHand=['pro_sup', 'deviation', 'flexion', 'cmc_abduction', 'cmc_flexion', 'mp_flexion', 'ip_flexion', 'mcp2_flexion', 'mcp2_abduction', 'pm2_flexion', 'md2_flexion', 'mcp3_flexion', 'mcp3_abduction', 'pm3_flexion', 'md3_flexion', 'mcp4_flexion', 'mcp4_abduction', 'pm4_flexion', 'md4_flexion', 'mcp5_flexion', 'mcp5_abduction', 'pm5_flexion', 'md5_flexion']

ASL_qpos={}
ASL_qpos[0]='0 0 0 0.5624 0.28272 -0.75573 -1.309 1.30045 -0.006982 1.45492 0.998897 1.26466 0 1.40604 0.227795 1.07614 -0.020944 1.46103 0.06284 0.83263 -0.14399 1.571 1.38248'.split(' ')
ASL_qpos[1]='0 0 0 0.0248 0.04536 -0.7854 -1.309 0.366605 0.010473 0.269258 0.111722 1.48459 0 1.45318 1.44532 1.44532 -0.204204 1.46103 1.44532 1.48459 -0.2618 1.47674 1.48459'.split(' ')
ASL_qpos[2]='0 0 0 0.0248 0.04536 -0.7854 -1.13447 0.514973 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 1.44532 -0.204204 1.46103 1.44532 1.48459 -0.2618 1.47674 1.48459'.split(' ')
ASL_qpos[3]='0 0 0 0.3384 0.25305 0.01569 -0.0262045 0.645885 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 1.571 -0.036652 1.52387 1.45318 1.40604 -0.068068 1.39033 1.571'.split(' ')
ASL_qpos[4]='0 0 0 0.6392 -0.147495 -0.7854 -1.309 0.637158 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 0.306345 -0.010472 0.400605 0.133535 0.21994 -0.068068 0.274925 0.01571'.split(' ')
ASL_qpos[5]='0 0 0 0.3384 0.25305 0.01569 -0.0262045 0.645885 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 0.306345 -0.010472 0.400605 0.133535 0.21994 -0.068068 0.274925 0.01571'.split(' ')
ASL_qpos[6]='0 0 0 0.6392 -0.147495 -0.7854 -1.309 0.637158 0.010473 0.128305 0.111722 0.510575 0 0.37704 0.117825 0.306345 -0.010472 0.400605 0.133535 1.1861 -0.2618 1.35891 1.48459'.split(' ')
ASL_qpos[7]='0 0 0 0.524 0.01569 -0.7854 -1.309 0.645885 -0.006982 0.128305 0.111722 0.510575 0 0.37704 0.117825 1.28036 -0.115192 1.52387 1.45318 0.432025 -0.068068 0.18852 0.149245'.split(' ')
ASL_qpos[8]='0 0 0 0.428 0.22338 -0.7854 -1.309 0.645885 -0.006982 0.128305 0.194636 1.39033 0 1.08399 0.573415 0.667675 -0.020944 0 0.06284 0.432025 -0.068068 0.18852 0.149245'.split(' ')
ASL_qpos[9]='0 0 0 0.5624 0.28272 -0.75573 -1.309 1.30045 -0.006982 1.45492 0.998897 0.39275 0 0.18852 0.227795 0.667675 -0.020944 0 0.06284 0.432025 -0.068068 0.18852 0.149245'.split(' ')

# ASl Eval envs for each numerals
for k in ASL_qpos.keys():
    register(id='myoHandPose'+str(k)+'Fixed-v0',
            entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
            max_episode_steps=100,
            kwargs={
                'model_path': curr_dir+'/assets/hand/2nd_hand_pose.xml',
                'viz_site_targets': ('THtip','IFtip','MFtip','RFtip','LFtip'),
                'target_jnt_value': np.array(ASL_qpos[k],'float'),
                'normalize_act': True,
                'pose_thd': .7,
                'reset_type': "init",        # none, init, random
                'target_type': 'fixed',      # switch / generate/ fixed
            }
    )

# ASL Train Env
m = np.array([ASL_qpos[i] for i in range(10)]).astype(float)
Rpos = {}
for i_n, n  in enumerate(jnt_namesHand):
    Rpos[n]=(np.min(m[:,i_n]), np.max(m[:,i_n]))

register(id='myoHandPoseRandom-v0',  #reconsider
        entry_point='mj_envs.envs.myo.pose_v0:PoseEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_pose.xml',
            'viz_site_targets': ('THtip','IFtip','MFtip','RFtip','LFtip'),
            'target_jnt_range': Rpos,
            'normalize_act': True,
            'pose_thd': .7,
            'reset_type': "random",         # none, init, random
            'target_type': 'generate',      # switch / generate/ fixed
        }
    )

# Hand-Joint Reaching ==============================
register(id='myoHandReachFixed-v0',
        entry_point='mj_envs.envs.myo.reach_v0:ReachEnvV0',
        max_episode_steps=100,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_pose.xml',
            'target_reach_range': {
                'THtip': ((-0.165, -0.217, 1.095), (-0.165, -0.217, 1.095)),
                'IFtip': ((-0.151, -0.227, 1.055), (-0.151, -0.227, 1.055)),
                'MFtip': ((-0.146, -0.227, 1.047), (-0.146, -0.227, 1.047)),
                'RFtip': ((-0.148, -0.223, 1.045), (-0.148, -0.223, 1.045)),
                'LFtip': ((-0.148, -0.208, 1.034), (-0.148, -0.208, 1.034)),
                },
            'normalize_act': True,
            'far_th': 0.044
        }
    )

register(id='myoHandReachRandom-v0',
    entry_point='mj_envs.envs.myo.reach_v0:ReachEnvV0',
    max_episode_steps=100,
    kwargs={
        'model_path': curr_dir+'/assets/hand/2nd_hand_pose.xml',
        'target_reach_range': {
            'THtip': ((-0.165-0.020, -0.217-0.040, 1.095-0.040), (-0.165+0.040, -0.217+0.020, 1.095+0.040)),
            'IFtip': ((-0.151-0.040, -0.227-0.020, 1.055-0.010), (-0.151+0.040, -0.227+0.020, 1.055+0.010)),
            'MFtip': ((-0.146-0.040, -0.227-0.020, 1.047-0.010), (-0.146+0.040, -0.227+0.020, 1.047+0.010)),
            'RFtip': ((-0.148-0.040, -0.223-0.020, 1.045-0.010), (-0.148+0.040, -0.223+0.020, 1.045+0.010)),
            'LFtip': ((-0.148-0.040, -0.208-0.020, 1.034-0.010), (-0.148+0.040, -0.208+0.020, 1.034+0.010)),

            },
        'normalize_act': True,
        'far_th': 0.034
    }
)

# Hand-Joint key turn ==============================
register(id='myoHandKeyTurnFixed-v0',
        entry_point='mj_envs.envs.myo.key_turn_v0:KeyTurnEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_Index_Thumb_keyturn.xml',
            'normalize_act': True
        }
    )

register(id='myoHandKeyTurnRandom-v0',
        entry_point='mj_envs.envs.myo.key_turn_v0:KeyTurnEnvV0',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_Index_Thumb_keyturn.xml',
            'normalize_act': True,
            'key_init_range':(-np.pi/2, np.pi/2),
            'goal_th': 2*np.pi
        }
    )


# Hold objects ==============================
register(id='myoHandObjHoldFixed-v0',
        entry_point='mj_envs.envs.myo.obj_hold_v0:ObjHoldFixedEnvV0',
        max_episode_steps=75,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_hold.xml',
            'normalize_act': True
        }
    )

register(id='myoHandObjHoldRandom-v0', # revisit
        entry_point='mj_envs.envs.myo.obj_hold_v0:ObjHoldRandomEnvV0',
        max_episode_steps=75,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_hold.xml',
            'normalize_act': True
        }
    )


# Pen twirl ==============================
register(id='myoHandPenTwirlFixed-v0',
            entry_point='mj_envs.envs.myo.pen_v0:PenTwirlFixedEnvV0',
            max_episode_steps=50,
            kwargs={
                'model_path': curr_dir+'/assets/hand/2nd_hand_pen.xml',
                'normalize_act': True,
                'frame_skip': 5,
            }
    )

register(id='myoHandPenTwirlRandom-v0',
        entry_point='mj_envs.envs.myo.pen_v0:PenTwirlRandomEnvV0',
        max_episode_steps=50,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_pen.xml',
            'normalize_act': True,
            'frame_skip': 5,
        }
    )

# Baoding ==============================
register(id='myoHandBaodingFixed-v1',
        entry_point='mj_envs.envs.myo.baoding_v1:BaodingFixedEnvV1',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_baoding.xml',
            'normalize_act': True,
            'reward_option': 0,
        }
    )
register(id='myoHandBaodingRandom-v1',
        entry_point='mj_envs.envs.myo.baoding_v1:BaodingRandomEnvV1',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_baoding.xml',
            'normalize_act': True,
            'reward_option': 0,
        }
    )
register(id='myoHandBaodingFixed4th-v1',
        entry_point='mj_envs.envs.myo.baoding_v1:BaodingFixedEnvV1',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_baoding.xml',
            'normalize_act': True,
            'n_shifts_per_period':4,
        }
    )
register(id='myoHandBaodingFixed8th-v1',
        entry_point='mj_envs.envs.myo.baoding_v1:BaodingFixedEnvV1',
        max_episode_steps=200,
        kwargs={
            'model_path': curr_dir+'/assets/hand/2nd_hand_baoding.xml',
            'normalize_act': True,
            'n_shifts_per_period':8,
        }
    )
