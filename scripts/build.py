try:
    from datapackage_utilities import building
except ImportError:
    raise ImportError("Missing datapackage-utilities package...")

building.infer_metadata(package_name='Bordelum', keep_resources=False,
                        foreign_keys={
                            'bus': ['dispatchable_generator', 'shortage',
                                    'volatile_generator', 'demand', 'excess',
                                    'battery-storage'],
                            'profile': ['volatile_generator', 'demand'],
                            'from_to_bus': ['transshipment']})
