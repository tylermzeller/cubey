import math
import colorama
colorama.init()

colors = {
    "WHITE": 0,
    "YELLOW": 1,
    "BLUE": 2,
    "GREEN": 3,
    "RED": 4,
    "PURPLE": 5
}

color_strings = {
    0: colorama.Fore.WHITE + 'W',
    1: colorama.Fore.YELLOW + 'Y',
    2: colorama.Fore.BLUE + 'B',
    3: colorama.Fore.GREEN + 'G',
    4: colorama.Fore.RED + 'R',
    5: colorama.Fore.MAGENTA + 'P',
}

DIMENSION = 3
LAST = DIMENSION - 1
FIRST = 0

iter_dim = range(DIMENSION)

class Cube(object):
    def __init__(self):
        self.to_solved()

    def __eq__(self, other):
        if isinstance(other, Cube):
            return (self._F == other._F and self._B == other._B and
                    self._R == other._R and self._L == other._L and
                    self._U == other._U and self._D == other._D)
        else:
            return False

    '''
    ---------------------------------------------------------------------------
    |    Public Methods:                                                      |
    ---------------------------------------------------------------------------
    '''

    # Turn the right face clockwise. Affects faces F, D, U, B
    def r(self):
        # First create a temporary buffer holding the front face's right col
        temp = Cube._get_col(self._F, LAST)

        # Second, swap the temporary buffer (which currently contains the front)
        # right col) with the right column of the up face
        Cube._swap(temp, self._U, col=LAST)
        # Third, swap the temporary buffer with the *LEFT* column of the back face
        Cube._swap(temp, self._B, col=FIRST, reverse=True)
        # Fourth, swap the temporary buffer with the right column of the down face
        Cube._swap(temp, self._D, col=LAST, reverse=True)
        # Fifth, swap the buffer with the right column of the front face (where we started)
        Cube._swap(temp, self._F, col=LAST)

        Cube._rotate_face_cw(self._R)

    # Turn the right face counter-clockwise. Affects faces F, D, U, B
    def r_prime(self):
        # First create a temporary buffer for swapping rows and cols btw faces
        temp = Cube._get_col(self._F, LAST)

        # Second, swap the temporary buffer (which currently contains the front)
        # right col) with the right column of the down face
        Cube._swap(temp, self._D, col=LAST)
        # Third, swap the temporary buffer with the *LEFT* column of the back face
        Cube._swap(temp, self._B, col=FIRST, reverse=True)
        # Fourth, swap the temporary buffer with the right column of the up face
        Cube._swap(temp, self._U, col=LAST, reverse=True)
        # Fifth, swap the buffer with the right column of the front face (where we started)
        Cube._swap(temp, self._F, col=LAST)

        Cube._rotate_face_ccw(self._R)

    def r2(self):
        self.r()
        self.r()

    def l(self):
        # First create a temporary buffer holding the front face's left col
        temp = Cube._get_col(self._F, FIRST)

        # Second, swap the temporary buffer (which currently contains the front)
        # left col) with the left column of the down face
        Cube._swap(temp, self._D, col=FIRST)
        # Third, swap the temporary buffer with the *RIGHT* column of the back face
        Cube._swap(temp, self._B, col=LAST, reverse=True)
        # Fourth, swap the temporary buffer with the left column of the up face
        Cube._swap(temp, self._U, col=FIRST, reverse=True)
        # Fifth, swap the buffer with the left column of the front face (where we started)
        Cube._swap(temp, self._F, col=FIRST)

        Cube._rotate_face_cw(self._L)

    def l_prime(self):
        # First create a temporary buffer holding the front face's left col
        temp = Cube._get_col(self._F, FIRST)

        # Second, swap the temporary buffer (which currently contains the front)
        # left col) with the left column of the up face
        Cube._swap(temp, self._U, col=FIRST)
        # Third, swap the temporary buffer with the *RIGHT* column of the back face
        Cube._swap(temp, self._B, col=LAST, reverse=True)
        # Fourth, swap the temporary buffer with the left column of the down face
        Cube._swap(temp, self._D, col=FIRST, reverse=True)
        # Fifth, swap the buffer with the left column of the front face (where we started)
        Cube._swap(temp, self._F, col=FIRST)

        Cube._rotate_face_ccw(self._L)

    def l2(self):
        self.l()
        self.l()

    def u(self):
        # First create a temporary buffer holding the front face's first row
        temp = Cube._get_row(self._F, FIRST)

        # Second, swap the temporary buffer (which currently contains the front)
        # top row) with the first row of the left face
        Cube._swap(temp, self._L, row=FIRST)
        # Third, swap the temporary buffer with the first row of the back face
        Cube._swap(temp, self._B, row=FIRST)
        # Fourth, swap the temporary buffer with the first row of the right face
        Cube._swap(temp, self._R, row=FIRST)
        # Fifth, swap the buffer with the first row of the front face (where we started)
        Cube._swap(temp, self._F, row=FIRST)

        Cube._rotate_face_cw(self._U)

    def u_prime(self):
        # First create a temporary buffer holding the front face's first row
        temp = Cube._get_row(self._F, FIRST)

        # Second, swap the temporary buffer (which currently contains the front)
        # top row) with the first row of the right face
        Cube._swap(temp, self._R, row=FIRST)
        # Third, swap the temporary buffer with the first row of the back face
        Cube._swap(temp, self._B, row=FIRST)
        # Fourth, swap the temporary buffer with the first row of the left face
        Cube._swap(temp, self._L, row=FIRST)
        # Fifth, swap the buffer with the first row of the front face (where we started)
        Cube._swap(temp, self._F, row=FIRST)

        Cube._rotate_face_ccw(self._U)

    def u2(self):
        self.u()
        self.u()

    def d(self):
        # First create a temporary buffer holding the front face's last row
        temp = Cube._get_row(self._F, LAST)

        # Second, swap the temporary buffer (which currently contains the front)
        # top row) with the last row of the right face
        Cube._swap(temp, self._R, row=LAST)
        # Third, swap the temporary buffer with the last row of the back face
        Cube._swap(temp, self._B, row=LAST)
        # Fourth, swap the temporary buffer with the last row of the left face
        Cube._swap(temp, self._L, row=LAST)
        # Fifth, swap the buffer with the last row of the front face (where we started)
        Cube._swap(temp, self._F, row=LAST)

        Cube._rotate_face_cw(self._D)

    def d_prime(self):
        # First create a temporary buffer holding the front face's last row
        temp = Cube._get_row(self._F, LAST)

        # Second, swap the temporary buffer (which currently contains the front)
        # top row) with the last row of the left face
        Cube._swap(temp, self._L, row=LAST)
        # Third, swap the temporary buffer with the last row of the back face
        Cube._swap(temp, self._B, row=LAST)
        # Fourth, swap the temporary buffer with the last row of the right face
        Cube._swap(temp, self._R, row=LAST)
        # Fifth, swap the buffer with the last row of the front face (where we started)
        Cube._swap(temp, self._F, row=LAST)

        Cube._rotate_face_ccw(self._D)

    def d2(self):
        self.d()
        self.d()

    def f(self):
        # First create a temporary buffer holding the up face's last row
        temp = Cube._get_row(self._U, LAST)

        # Second, swap the temporary buffer (which currently contains the front)
        # top row) with the first row of the right face
        Cube._swap(temp, self._R, col=FIRST)
        # Third, swap the temporary buffer with the first row of the down face
        Cube._swap(temp, self._D, row=FIRST, reverse=True)
        # Fourth, swap the temporary buffer with the last col of the left face
        Cube._swap(temp, self._L, col=LAST)
        # Fifth, swap the buffer with the last row of the up face (where we started)
        Cube._swap(temp, self._U, row=LAST, reverse=True)

        Cube._rotate_face_cw(self._F)

    def f_prime(self):
        # First create a temporary buffer holding the up face's last row
        temp = Cube._get_row(self._U, LAST)

        # Second, swap the temporary buffer (which currently contains the front)
        # top row) with the last row of the left face
        Cube._swap(temp, self._L, col=LAST, reverse=True)
        # Third, swap the temporary buffer with the last row of the back face
        Cube._swap(temp, self._D, row=FIRST)
        # Fourth, swap the temporary buffer with the last row of the right face
        Cube._swap(temp, self._R, col=FIRST, reverse=True)
        # Fifth, swap the buffer with the last row of the front face (where we started)
        Cube._swap(temp, self._U, row=LAST)

        Cube._rotate_face_ccw(self._F)

    def f2(self):
        self.f()
        self.f()

    def b(self):
        # First create a temporary buffer holding the up face's first row
        temp = Cube._get_row(self._U, FIRST)

        # Second, swap the temporary buffer (which currently contains the front)
        # top row) with the last row of the left face
        Cube._swap(temp, self._L, col=FIRST, reverse=True)
        # Third, swap the temporary buffer with the last row of the back face
        Cube._swap(temp, self._D, row=LAST)
        # Fourth, swap the temporary buffer with the last row of the right face
        Cube._swap(temp, self._R, col=LAST, reverse=True)
        # Fifth, swap the buffer with the last row of the front face (where we started)
        Cube._swap(temp, self._U, row=FIRST)

        Cube._rotate_face_cw(self._B)

    def b_prime(self):
        # First create a temporary buffer holding the up face's last row
        temp = Cube._get_row(self._U, FIRST)

        # Second, swap the temporary buffer (which currently contains the front)
        # top row) with the last row of the left face
        Cube._swap(temp, self._R, col=LAST)
        # Third, swap the temporary buffer with the last row of the back face
        Cube._swap(temp, self._D, row=LAST, reverse=True)
        # Fourth, swap the temporary buffer with the last row of the right face
        Cube._swap(temp, self._L, col=FIRST)
        # Fifth, swap the buffer with the last row of the front face (where we started)
        Cube._swap(temp, self._U, row=FIRST, reverse=True)

        Cube._rotate_face_ccw(self._B)

    def b2(self):
        self.b()
        self.b()

    def is_solved(self):
        for face in [self._F, self._B, self._L, self._R, self._U, self._D]:
            for row in face:
                return all([elm == face[DIMENSION / 2][DIMENSION / 2] for elm in row])

    def to_solved(self):
        self._F = [[colors['RED'] for j in iter_dim] for i in iter_dim]
        self._B = [[colors['PURPLE'] for j in iter_dim] for i in iter_dim]
        self._L = [[colors['GREEN'] for j in iter_dim] for i in iter_dim]
        self._R = [[colors['BLUE'] for j in iter_dim] for i in iter_dim]
        self._U = [[colors['WHITE'] for j in iter_dim] for i in iter_dim]
        self._D = [[colors['YELLOW'] for j in iter_dim] for i in iter_dim]

    def to_checker(self):
        if not self.is_solved():
            self.to_solved()
        self.l2()
        self.r2()
        self.f2()
        self.b2()
        self.u2()
        self.d2()

    def to_centers(self, times=1):
        if not self.is_solved():
            self.to_solved()

        times = max(times, 0)
        times_to_solve = 3
        times %= times_to_solve
        for i in range(times):
            self.r()
            self.l_prime()
            self.u()
            self.d_prime()
            self.f_prime()
            self.b()
            self.r()
            self.l_prime()

    def trigger(self, times=1):
        times = max(times, 0)
        times_to_solve = 4
        times %= times_to_solve
        for i in range(times):
            self.r()
            self.u()
            self.r_prime()

    def trigger_u2(self, times=1):
        times = max(times, 0)
        times_to_solve = 2
        times %= times_to_solve
        for i in range(times):
            self.r()
            self.u2()
            self.r_prime()

    def sune(self, times=1):
        times = max(times, 0)
        times_to_solve = 6
        times %= times_to_solve
        for i in range(times):
            self.trigger()
            self.u()
            self.trigger_u2()

    '''
    ---------------------------------------------------------------------------
    |    Helper Methods:                                                      |
    ---------------------------------------------------------------------------
    '''

    # Swaps the elements in the buffer list with the cooresponding row or col of the face
    @staticmethod
    def _swap(swap_buffer, face, row=None, col=None, reverse=False):
        if (col != None and row != None) or (col == None and row == None):
            print('Invalid use of _swap. Supply row or col.')
            return

        # Swap between the swap_buffer and the face along the specified column
        if col != None:
            column = Cube._get_col(face, col)
            Cube._swap_row_or_col(swap_buffer, column)

            if reverse:
                column.reverse()

            # We have to manually add back the swapped column, because there is
            # no way to get a mutable reference to a standard 2D list's column
            Cube._set_col(face, column, col)

        # Swap between the swap_buffer and the face along the specified row
        elif row != None:
            # {r} is a (mutable) reference to the current face's row. Because
            # of this we don't need to set explicitly the row of the face after.
            _row = Cube._get_row(face, row)
            Cube._swap_row_or_col(swap_buffer, _row)

            # if reverse:
            #     _row.reverse()

    # Face *MUST* be a square matrix
    @staticmethod
    def _rotate_face_cw(face):
        dim = len(face)
        if dim <= 1:
            # Cant rotate a single edge
            return

        # number of edges *per top row!* (number of pieces in the top row minus
        # 2 corners)
        num_edges = dim - 2
        first = 0
        last = dim - 1

        # swap all the edges
        for i in range(num_edges):
            temp_edge = face[first][i + 1]
            temp_edge = Cube._swap_piece(temp_edge, face, i + 1, last)
            temp_edge = Cube._swap_piece(temp_edge, face, last, last - (i + 1))
            temp_edge = Cube._swap_piece(temp_edge, face, last - (i + 1), first)
            temp_edge = Cube._swap_piece(temp_edge, face, first, last - (i + 1))

        # swap all the corners
        temp_corner = face[first][first]
        temp_corner = Cube._swap_piece(temp_corner, face, first, last)
        temp_corner = Cube._swap_piece(temp_corner, face, last, last)
        temp_corner = Cube._swap_piece(temp_corner, face, last, first)
        temp_corner = Cube._swap_piece(temp_corner, face, first, first)

        inner_face = Cube._get_inner_face(face)

        # Rotate the inner layers
        Cube._rotate_face_cw(inner_face)

    @staticmethod
    def _rotate_face_ccw(face):
        dim = len(face)
        if dim <= 1:
            # Cant rotate a single edge
            return

        # number of edges *per top row!* (number of pieces in the top row minus
        # 2 corners)
        num_edges = dim - 2
        first = 0
        last = dim - 1

        # swap all the edges
        for i in range(num_edges):
            temp_edge = face[FIRST][i + 1]
            temp_edge = Cube._swap_piece(temp_edge, face, i + 1, first)
            temp_edge = Cube._swap_piece(temp_edge, face, last, (i + 1))
            temp_edge = Cube._swap_piece(temp_edge, face, last - (i + 1), last)
            temp_edge = Cube._swap_piece(temp_edge, face, first, last - (i + 1))

        # swap all the corners
        temp_corner = face[FIRST][FIRST]
        temp_corner = Cube._swap_piece(temp_corner, face, last, first)
        temp_corner = Cube._swap_piece(temp_corner, face, last, last)
        temp_corner = Cube._swap_piece(temp_corner, face, first, last)
        temp_corner = Cube._swap_piece(temp_corner, face, first, first)

        inner_face = Cube._get_inner_face(face)

        # Rotate the inner layers
        Cube._rotate_face_cw(inner_face)

    @staticmethod
    def _get_inner_face(face):
        inner_rows = face[1:len(face) - 1]
        inner_face = []
        for row in inner_rows:
            inner_face.append(row[1:len(face) - 1])
        return inner_face

    @staticmethod
    def _swap_piece(temp_piece, face, row=0, col=0):
        piece_buffer = face[row][col]
        face[row][col] = temp_piece
        return piece_buffer

    @staticmethod
    def _get_row_or_col(face, row=None, col=None):
        if col != None:
            return Cube._get_col(face, col)
        elif row != None:
            return Cube._get_row(face, row)

    @staticmethod
    def _set_row_or_col(face, row_or_col, row=None, col=None):
        if col != None:
            return Cube._set_col(face, row_or_col, col)
        elif row != None:
            return Cube._set_row(face, row_or_col, row)

    @staticmethod
    def _swap_row_or_col(swap_buffer, row_or_col):
        temp_buffer = row_or_col[:]
        row_or_col[:] = swap_buffer[:]
        swap_buffer[:] = temp_buffer

    @staticmethod
    def _get_col(face, col=0):
        return [row[col] for row in face]

    @staticmethod
    def _get_row(face, row=0):
        return face[row]

    @staticmethod
    def _set_col(face, col_buffer, col=0):
        for r in iter_dim:
            face[r][col] = col_buffer[r]

    @staticmethod
    def _set_row(face, row_buffer, row=0):
        face[row] = row_buffer[:]

    # {face} *MUST* be a 2D list. Returns a list of length {len(face) * len(face[0])}
    # of the elements of face ordered by column.
    ''' Example:
    > a = [[random.randint(1,100) for x in range(3)] for y in range(3)]
    #=> a =
    #=>     [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
    > b = _flatten_face_columns(a)
    #=> b =
    #=>     [49, 80, 20, 84, 7, 34, 51, 37, 70]
    '''
    @staticmethod
    def _flatten_face_columns(face):
        return [face[i][j] for j in range(len(face[0])) for i in range(len(face))]

    # {face} *MUST* be a 2D list. Returns a list of length {len(face) * len(face[0])}
    # of the elements of face ordered by row.
    ''' Example:
    > a = [[random.randint(1,100) for x in range(3)] for y in range(3)]
    #=> a =
    #=>     [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
    > b = _flatten_face_rows(a)
    #=> b =
    #=>     [49, 84, 51, 80, 7, 37, 20, 34, 70]
    '''
    @staticmethod
    def _flatten_face_rows(face):
        return [face[i][j] for i in range(len(face)) for j in range(len(face[0]))]

    # Reconstructs a 2D list of a flattened column-ordered list.
    '''
        Example:
        > a = [[random.randint(1,100) for x in range(3)] for y in range(3)]
        #=> a =
        #=>     [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
        > b = _flatten_face_columns(a)
        #=> b =
        #=>     [49, 80, 20, 84, 7, 34, 51, 37, 70]
        > c = _reconstruct_face_columns(b)
        #=> c =
        #=>     [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
    '''
    @staticmethod
    def _reconstruct_face_columns(flat_face):
        return [[flat_face[DIMENSION * i + j] for i in iter_dim] for j in iter_dim]

    # Reconstructs a 2D list of a flattened column-ordered list.
    '''
        Example:
        > a = [[random.randint(1,100) for x in range(3)] for y in range(3)]
        #=> a =
        #=>     [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
        > b = _flatten_face_rows(a)
        #=> b =
        #=>     [49, 84, 51, 80, 7, 37, 20, 34, 70]
        > c = _reconstruct_face_rows(b)
        #=> c =
        #=>     [[49, 84, 51], [80, 7, 37], [20, 34, 70]]
    '''
    @staticmethod
    def _reconstruct_face_rows(flat_face):
        return [[flat_face[DIMENSION * i + j] for j in iter_dim] for i in iter_dim]

    def __str__(self):
        string = ''

        # Stringify all dimensions of the cube plus 1 for the header string
        for i in range(DIMENSION + 1):
            # First print the head string
            if i == 0:
                space = ' ' * DIMENSION
                first_space = ' ' * (DIMENSION / 2)
                # The below order is the same order we add in the init method
                string += colorama.Fore.BLACK + first_space + 'F' + space +  'B' + space +  'L' + space +  'R' + space +  'U' + space +  'D\n'
            # Next print each row of each face
            else:
                for face in [self._F, self._B, self._L, self._R, self._U, self._D]:
                    for j in iter_dim:
                        string += color_strings[face[i - 1][j]]
                    string += ' '
                string += '\n'
        string += colorama.Style.RESET_ALL
        return string
