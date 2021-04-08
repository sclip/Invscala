import os
import music21


class MIDI:
    @staticmethod
    def write(stream, path=None, backup_path=None):
        if path is None:
            path = os.path.expanduser('~/documents/Scale Finder/MIDI/')
        if backup_path is None:
            backup_path = "res/MIDI/"
        try:
            stream.write("midi", path)
        except PermissionError:
            print(f"Error: Permission Denied, unable to write MIDI {s} to {path}")
            print("Writing to backup folder")
            try:
                stream.write("midi", backup_path)
            except PermissionError:
                print(f"Error: Permission Denied, unable to write MIDI {s} to {backup_path}")
                print("Try launching the program as admin")
                return False
            except FileNotFoundError:
                print(f"Error: No such file or directory: {backup_path}")
                return False
        return True


if __name__ == '__main__':
    # This part is for testing
    s = music21.stream.Stream()
    s.append(music21.note.Note("A4"))
    MIDI.write(s, backup_path="../../data/MIDI")
