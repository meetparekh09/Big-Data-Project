import h5py
import numpy

hdf = h5py.File('data/A/A/A/TRAAAAW128F429D538.h5', 'r')
analysis_group = hdf['analysis']
metadata_group = hdf['metadata']
musicbrainz_group = hdf['musicbrainz']

print('\n\n')
print('Structure of Analysis Group')
for key in list(analysis_group.keys()):
    print(key, analysis_group[key].shape)


print('\n\n')
print('Structure of Metadata Group')
for key in list(metadata_group.keys()):
    print(key, metadata_group[key].shape)


print('\n\n')
print('Structure of Musicbrainz Group')
for key in list(musicbrainz_group.keys()):
    print(key, musicbrainz_group[key].shape)
