import argparse
import sys
from frankapy import FrankaArm
from frankapy import FrankaConstants as FC

def wait_for_enter():
    if sys.version_info[0] < 3:
        raw_input('Press Enter to continue:')
    else:
        input('Press Enter to continue:')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--time', '-t', type=float, default=10)
    parser.add_argument('--open_gripper', '-o', action='store_true')
    args = parser.parse_args()

    print('Starting robot')
    fa = FrankaArm()
    if args.open_gripper:
        fa.open_gripper()

    print('Be very careful!! Make sure the robot can safely move to HOME JOINTS Position.')
    wait_for_enter()

    fa.reset_joints()
    fa.goto_joints([9.55517455e-04,  5.70560164e-01, -3.71729893e-01, -2.13859476e+00, 2.11785138e-01,  2.69754226e+00,  1.89678873e+00], use_impedance=False, dynamic=False)
    
    
