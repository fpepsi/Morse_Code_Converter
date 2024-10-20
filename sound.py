import pygame
import time
import numpy as np

class MorseSound:
    def __init__(self):
        self.frequency = 1000  # Frequency of beep (in Hertz)
        self.duration_unit = 100   # Duration of beep in milliseconds (1 second)
        self.beep_dits = None
        self.beep_dahs = None


    # Function to generate a sound array for a beep
    def generate_beep(self, duration)-> object:
        '''creates a sound with a frequency defined in the class, and duration defined in miliseconds'''
        sample_rate = 44100  # CD quality
        t = np.linspace(0, duration / 1000, int(sample_rate * duration / 1000), False)
        sound_wave = 0.5 * np.sin(2 * np.pi * self.frequency * t)
        sound_wave = np.int16(sound_wave * 32767)  # Convert to 16-bit sound
        sound_wave = np.repeat(sound_wave[:, np.newaxis], 2, axis=1)  # Stereo
        return pygame.sndarray.make_sound(sound_wave)


    def play_morse_code(self, sentence_list: list, morse_code_list: list) -> None:
        '''receives a list with each morse code as an element, generates a list with the timing of each sound,
        and then play the sounds accordingly'''
        morse_code_list = morse_code_list
        pygame.mixer.init()
        sound_sequence = []
        self.beep_dits = self.generate_beep(self.duration_unit)
        self.beep_dahs = self.generate_beep(self.duration_unit * 3)
        for code, char in zip(morse_code_list, sentence_list):
            sound_sequence.append(char)
            sound_time = 0
            for char2 in code:
                if char2 == '▄':
                    sound_time += 1
                elif char2 == ' ':
                    if sound_time == 1:
                        sound_sequence.append('dits')
                    elif sound_time == 3:
                        sound_sequence.append('dahs')
                    sound_sequence.append('space')
                    sound_time = 0
            if sound_time == 1:
                sound_sequence.append('dits')
            elif sound_time == 3:
                sound_sequence.append('dahs')
            sound_sequence.append('end_of_char')

        for action in sound_sequence:
            if action == 'space':
                time.sleep(self.duration_unit / 1000)
            elif action == 'end_of_char':
                time.sleep(self.duration_unit * 7 / 1000)
            elif action == 'dits':
                self.beep_dits.play()
                time.sleep(self.duration_unit / 1000)  # Keep playing for the duration
                self.beep_dits.stop()
            elif action == 'dahs':
                self.beep_dahs.play()
                time.sleep(self.duration_unit * 3 / 1000)  # Keep playing for the duration
                self.beep_dahs.stop()
            else:
                print(action)
        pygame.mixer.quit()

# Play the morse code translation
# play_morse_code(morse_code_translation)


# Morse code translation test list
# morse_code_translation = ['▄ ▄▄▄', '▄▄▄ ▄ ▄ ▄', '▄▄▄ ▄ ▄▄▄ ▄', '▄▄▄ ▄ ▄']
