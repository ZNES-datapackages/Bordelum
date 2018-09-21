from datapackage_utilities import building

building.infer_metadata(package_name='Bordelum', keep_resources=False,
                        foreign_keys={
                            'bus': ['dispatchable-generator',
                                    'volatile-generator', 'demand', 'storage'],
                            'profile': ['volatile-generator', 'demand'],
                            'from_to_bus': ['transmission', 'conversion']})
