import StudentAgent as sa
import sys, getopt, json, traceback
import common

if __name__ == '__main__':
    studentAgent = sa.StudentAgent(verbose=True)
    parameters = {
        'verbose': False,
        'frames': "WhereExampleQuestions.json",
        'log': "results"
    }

    _frame_filename = parameters['frames']
    _verbose = parameters['verbose']

    try:
        with open(_frame_filename, encoding='utf-8') as json_data:
            _ground_truth_frames = json.load(json_data)
    except Exception as e:
        print("Failure opening or reading frames: " + str(e))

    for _ground_truth_dict in _ground_truth_frames:
        _ground_truth_frame = common.Frame.fromDict(_ground_truth_dict)
        _result_str = _ground_truth_frame.print('all')
        _agent_frame = studentAgent.input_output(_ground_truth_dict['question'])
        print(_agent_frame)
        print(_ground_truth_dict['object'],',',_ground_truth_dict['data_requested'])
        print()


