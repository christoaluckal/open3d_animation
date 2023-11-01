import json
import numpy as np

with open('ablation_traj.json', 'r') as f:
    data = json.load(f)

fps = 240

def interpolate(data):
    params = data['parameters']

    extrinsics = []

    dummy_dict = params[0]


    for i in range(len(params)):
        extrinsics.append(np.array(params[i]['extrinsic']))

    extrinsics = np.array(extrinsics)

    # interpolated_x = np.linspace(extrinsics[0][12], extrinsics[-1][12], total_frames)
    # interpolated_y = np.linspace(extrinsics[0][13], extrinsics[-1][13], total_frames)
    # interpolated_z = np.linspace(extrinsics[0][14], extrinsics[-1][14], total_frames)

    interpolated_dict = []

    # for i in range(total_frames):
    #     temp_dict = dummy_dict.copy()
    #     extrinsic_list = temp_dict['extrinsic'].copy()



    #     extrinsic_list[12] = round(interpolated_x[i],6)
    #     extrinsic_list[13] = round(interpolated_y[i],6)
    #     extrinsic_list[14] = round(interpolated_z[i],6)

    #     temp_dict['extrinsic'] = extrinsic_list


    #     interpolated_dict.append(temp_dict)

    for i in range(0,len(extrinsics)):
        if i == len(extrinsics)-1:
            break
        prev = extrinsics[i]
        next = extrinsics[i+1]
        interpolated_0 = np.linspace(prev[0], next[0], fps)
        interpolated_1 = np.linspace(prev[1], next[1], fps)
        interpolated_2 = np.linspace(prev[2], next[2], fps)
        interpolated_3 = np.linspace(prev[3], next[3], fps)
        interpolated_4 = np.linspace(prev[4], next[4], fps)
        interpolated_5 = np.linspace(prev[5], next[5], fps)
        interpolated_6 = np.linspace(prev[6], next[6], fps)
        interpolated_7 = np.linspace(prev[7], next[7], fps)
        interpolated_8 = np.linspace(prev[8], next[8], fps)
        interpolated_9 = np.linspace(prev[9], next[9], fps)
        interpolated_10 = np.linspace(prev[10], next[10], fps)
        interpolated_11 = np.linspace(prev[11], next[11], fps)
        interpolated_12 = np.linspace(prev[12], next[12], fps)
        interpolated_13 = np.linspace(prev[13], next[13], fps)
        interpolated_14 = np.linspace(prev[14], next[14], fps)
        interpolated_15 = np.linspace(prev[15], next[15], fps)

        for j in range(fps):
            temp_dict = dummy_dict.copy()
            extrinsic_list = temp_dict['extrinsic'].copy()

            extrinsic_list[0] = round(interpolated_0[j],6)
            extrinsic_list[1] = round(interpolated_1[j],6)
            extrinsic_list[2] = round(interpolated_2[j],6)
            extrinsic_list[3] = round(interpolated_3[j],6)
            extrinsic_list[4] = round(interpolated_4[j],6)
            extrinsic_list[5] = round(interpolated_5[j],6)
            extrinsic_list[6] = round(interpolated_6[j],6)
            extrinsic_list[7] = round(interpolated_7[j],6)
            extrinsic_list[8] = round(interpolated_8[j],6)
            extrinsic_list[9] = round(interpolated_9[j],6)
            extrinsic_list[10] = round(interpolated_10[j],6)
            extrinsic_list[11] = round(interpolated_11[j],6)
            extrinsic_list[12] = round(interpolated_12[j],6)
            extrinsic_list[13] = round(interpolated_13[j],6)
            extrinsic_list[14] = round(interpolated_14[j],6)
            extrinsic_list[15] = round(interpolated_15[j],6)

            temp_dict['extrinsic'] = extrinsic_list

            interpolated_dict.append(temp_dict)



    data['parameters'] = interpolated_dict

    return data


data2 = interpolate(data)

with open('interpolated_abj_trajectory.json', 'w') as f:
    json.dump(data2, f, indent=4)



