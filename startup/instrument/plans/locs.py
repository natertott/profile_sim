__all__ = ['loc177', 'loc177_flipy', 'loc177_flip1', 'locyale']
import numpy as np

y = [9.0, 4.5, 0.0, -4.5, -9.0, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, 
    -18.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, 
    27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, 
    -27.0, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, 
    -22.5, -27.0, 31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, 
    -13.5, -18.0, -22.5, -27.0, -31.5, 31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 
    4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, -27.0, -31.5, 31.5, 27.0, 22.5, 
    18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, -27.0, -31.5, 
    31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, 
    -22.5, -27.0, -31.5, 31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, 
    -9.0, -13.5, -18.0, -22.5, -27.0, -31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 
    0.0, -4.5, -9.0, -13.5, -18.0, -22.5, -27.0, 27.0, 22.5, 18.0, 13.5, 9.0,
    4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, -27.0, 22.5, 18.0, 13.5, 9.0, 
    4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, 18.0, 13.5, 9.0, 4.5, 0.0, 
    -4.5, -9.0, -13.5, -18.0, 9.0, 4.5, 0.0, -4.5, -9.0]

x = [-31.5, -31.5, -31.5, -31.5, -31.5, -27.0, -27.0, -27.0, -27.0, -27.0,
     -27.0, -27.0, -27.0, -27.0, -22.5, -22.5, -22.5, -22.5, -22.5, -22.5, 
     -22.5, -22.5, -22.5, -22.5, -22.5, -18.0, -18.0, -18.0, -18.0, -18.0,
    -18.0, -18.0, -18.0, -18.0, -18.0, -18.0, -18.0, -18.0, -13.5, -13.5,
    -13.5, -13.5, -13.5, -13.5, -13.5, -13.5, -13.5, -13.5, -13.5, -13.5,
    -13.5, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0,
    -9.0, -9.0, -9.0, -9.0, -9.0, -4.5, -4.5, -4.5, -4.5, -4.5, -4.5,
    -4.5, -4.5, -4.5, -4.5, -4.5, -4.5, -4.5, -4.5, -4.5, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5,
    4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 
    9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 
    9.0, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 
    13.5, 13.5, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 
    18.0, 18.0, 18.0, 22.5, 22.5, 22.5, 22.5, 22.5, 22.5, 22.5, 22.5, 22.5, 
    22.5, 22.5, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 31.5, 
    31.5, 31.5, 31.5, 31.5]

loc177 = np.array([x,y])
loc177_flipy = np.array([x,-1*np.array(y)])
loc177_flip1 = np.array([-1*np.array(x), -1*np.array(y)])

yalex=[-40. , -37.5, -35. , -32.5, -30. , -27.5, -25. , -22.5, -20. ,
       -17.5, -15. , -12.5, -10. ,  -7.5,  -5. ,  -2.5,   0. ,   2.5,
       5. ,   7.5,  10. ,  12.5,  15. ,  17.5,  20. ,  22.5,  25. ,
       27.5,  30. ,  32.5,  35. ,  37.5,  40. , -40. , -37.5, -35. ,
       -32.5, -30. , -27.5, -25. , -22.5, -20. , -17.5, -15. , -12.5,
       -10. ,  -7.5,  -5. ,  -2.5,   0. ,   2.5,   5. ,   7.5,  10. ,
       12.5,  15. ,  17.5,  20. ,  22.5,  25. ,  27.5,  30. ,  32.5,
       35. ,  37.5,  40. , -40. , -37.5, -35. , -32.5, -30. , -27.5,
       -25. , -22.5, -20. , -17.5, -15. , -12.5, -10. ,  -7.5,  -5. ,
       -2.5,   0. ,   2.5,   5. ,   7.5,  10. ,  12.5,  15. ,  17.5,
       20. ,  22.5,  25. ,  27.5,  30. ,  32.5,  35. ,  37.5,  40. ,
       -40. , -37.5, -35. , -32.5, -30. , -27.5, -25. , -22.5, -20. ,
       -17.5, -15. , -12.5, -10. ,  -7.5,  -5. ,  -2.5,   0. ,   2.5,
       5. ,   7.5,  10. ,  12.5,  15. ,  17.5,  20. ,  22.5,  25. ,
       27.5,  30. ,  32.5,  35. ,  37.5,  40. , -40. , -37.5, -35. ,
       -32.5, -30. , -27.5, -25. , -22.5, -20. , -17.5, -15. , -12.5,
       -10. ,  -7.5,  -5. ,  -2.5,   0. ,   2.5,   5. ,   7.5,  10. ,
       12.5,  15. ,  17.5,  20. ,  22.5,  25. ,  27.5,  30. ,  32.5,
       35. ,  37.5,  40. , -40. , -37.5, -35. , -32.5, -30. , -27.5,
       -25. , -22.5, -20. , -17.5, -15. , -12.5, -10. ,  -7.5,  -5. ,
       -2.5,   0. ,   2.5,   5. ,   7.5,  10. ,  12.5,  15. ,  17.5,
       20. ,  22.5,  25. ,  27.5,  30. ,  32.5,  35. ,  37.5,  40. ]

yaley=[-17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -17.5,
      -17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -17.5,
      -17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -17.5,
      -17.5, -17.5, -17.5, -17.5, -17.5, -17.5, -10.5, -10.5, -10.5,
      -10.5, -10.5, -10.5, -10.5, -10.5, -10.5, -10.5, -10.5, -10.5,
      -10.5, -10.5, -10.5, -10.5, -10.5, -10.5, -10.5, -10.5, -10.5,
      -10.5, -10.5, -10.5, -10.5, -10.5, -10.5, -10.5, -10.5, -10.5,
      -10.5, -10.5, -10.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,
      -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,
      -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,
      -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,  -3.5,
      3.5,   3.5,   3.5,   3.5,   3.5,   3.5,   3.5,   3.5,   3.5,
      3.5,   3.5,   3.5,   3.5,   3.5,   3.5,   3.5,   3.5,   3.5,
      3.5,   3.5,   3.5,   3.5,   3.5,   3.5,   3.5,   3.5,   3.5,
      3.5,   3.5,   3.5,   3.5,   3.5,   3.5,  10.5,  10.5,  10.5,
      10.5,  10.5,  10.5,  10.5,  10.5,  10.5,  10.5,  10.5,  10.5,
      10.5,  10.5,  10.5,  10.5,  10.5,  10.5,  10.5,  10.5,  10.5,
      10.5,  10.5,  10.5,  10.5,  10.5,  10.5,  10.5,  10.5,  10.5,
      10.5,  10.5,  10.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5,
      17.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5,
      17.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5,
      17.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5,  17.5]

_locyale = np.array([yalex, yaley])
locyale = np.array([-np.array(yaley), yalex])