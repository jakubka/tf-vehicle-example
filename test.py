import os
from find_vehicle_in_image import find_vehicle_in_image

def test_vehicle_detection_file(file_path):
    file_name = os.path.basename(file_path)

    detected_vehicle = find_vehicle_in_image(file_path)
    expected_vehicle = file_name.split('_')[0]

    correct = expected_vehicle == detected_vehicle
    print(f'{file_name}: {"✅" if correct else "🔴"} {detected_vehicle if not correct else ""}')


def test_vehicle_detection_folder(folder_path):
    files = sorted(os.listdir(folder_path))
    for file_name in files:
        if '.jpg' not in file_name:
            continue
        
        test_vehicle_detection_file(os.path.join(folder_path, file_name))
    
test_vehicle_detection_folder('test_data')
# test_vehicle_detection_file('test_data/bus_1.jpg')