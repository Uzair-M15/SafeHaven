import lib.shErrors as shErrors
import numpy

class VectorWeightEncryption:
    def encrypt(text : str):
        weights = [3510, 84, 684]
        mat = []
        if not text == '':
            for char in text:
                curr_vec = []
                for weight in weights:
                    curr_vec.append(ord(char) * weight)
                mat.append(curr_vec)
        else:
            return shErrors.error_code(shErrors.FORBIDDEN , 'crypt.encrypt requires text but none was given').__str__()

        return mat