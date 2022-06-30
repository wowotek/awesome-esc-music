# keywords = {
#     "#song_name": "SONG_NAME",
#     "#artist": "SONG_ARTIST",
#     "#recommended_motor_count": "SONG_MOTOR_COUNT",
#     "@+": "TRACK_START",
#     "@-": "TRACK_END",
#     "+track_name": "TRACK_NAME",
#     "+motor_options": "TRACK_MOTOR_SELECTION",
#     "+general_length": "TRACK_GENERAL_LENGTH",
#     "+general_interval": "TRACK_GENERAL_INTERVAL",
#     "+notes": "TRACK_NOTES"
# }

# def read_escm_file(target_file):
#     data_lines = []
#     with open(target_file) as f:
#         for i in f.readlines():
#             r = i.replace("\n", "")
#             if r:
#                 data_lines.append(r)
    
#     return data_lines

# def separate_tracks(data_lines):
#     tracks = []
    
#     line_index = 0
#     while line_index < len(data_lines):
#         # Track Start
#         if "@+" == data_lines[line_index]:
#             entry = []
#             while data_lines[line_index] != "@-":
#                 line_index += 1
#                 entry.append(data_lines[line_index])
#             entry.pop()
#             tracks.append(entry)
        
#         line_index += 1
    
#     return tracks

# def describe_tracks(tracks):
#     described_tracks = []
#     for track in tracks:
#         described = {}
#         for entry in track:
#             entry_keywords = [
#                 "+track_name",
#                 "+motor_options",
#                 "+general_length",
#                 "+general_interval",
#                 "+notes",
#             ]
#             for keyword in entry_keywords:
#                 if keyword in entry:
#                     track_name = entry.split(" ")
#                     track_name.pop(0) 
#                     described[keywords[keyword]] = " ".join(track_name)
#         described_tracks.append(described)
    
#     return described_tracks

# file = read_escm_file("musics/kobo_kanaeru-mantra_hujan.escm")
# tracks = separate_tracks(file)
# described_tracks = describe_tracks(tracks)
# print(described_tracks)