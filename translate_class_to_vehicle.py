mapping = {
 'ambulance': 'car',
 'bicycle-built-for-two': 'bicycle',
 'cab': 'car',
 'convertible': 'car',
 'cruiser': 'motorcycle',
 'fire_engine': 'truck',
 'freight_car': 'train',
 'garbage_truck': 'truck',
 'harvester': 'harvester',
 'limousine': 'car',
 'minibus': 'bus',
 'moped': 'motorcycle',
 'motor_scooter': 'motorcycle',
 'mountain_bike': 'bicycle',
 'moving_van': 'truck',
 'race_car': 'car',
 'scooter': 'motorcycle',
 'snowplow': 'snowplow',
 'sports_car': 'car',
 'steam_locomotive': 'train',
 'taxi': 'car',
 'tow_truck': 'truck',
 'tractor': 'tractor',
 'trailer_truck': 'truck',
 'train': 'train',
 'trolleybus': 'bus',
 'unicycle': 'bicycle',
}

def map_class_to_vehicle(imagenet_class):
    res = mapping.get(imagenet_class)
    if res is None:
        print(f'WARN, cant map {imagenet_class}')
    return res