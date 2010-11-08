#<pre>Copyright 2006 The Closure Library Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.</pre>


from goog.array import map, reduce


def randomInt(a):
  return Math.floor(Math.random() * a)


def uniformRandom(a, b):
  'sample from [a, b)'
  return a + Math.random() * (b - a)


def clamp(value, min, max):
  return Math.min(Math.max(value, min), max)


def modulo(a, b):
  r = a % b;
  # If r and b differ in sign, add b to wrap the result to the correct sign.
  return r + b if (r * b < 0) else r


def lerp(a, b, x):
  return a + x * (b - a)


def nearlyEquals(a, b, opt_tolerance):
  return Math.abs(a - b) <= (opt_tolerance or 0.000001)


def standardAngle(angle):
  return modulo(angle, 360)


def toRadians(angleDegrees):
  return angleDegrees * Math.PI / 180


def toDegrees(angleRadians):
  return angleRadians * 180 / Math.PI


def angleDx(degrees, radius):
  return radius * Math.cos(toRadians(degrees))


def angleDy(degrees, radius):
  return radius * Math.sin(toRadians(degrees))


def angle(x1, y1, x2, y2):
  return standardAngle(toDegrees(Math.atan2(y2 - y1, x2 - x1)))


def angleDifference(startAngle, endAngle):
  d = standardAngle(endAngle) - standardAngle(startAngle)
  if (d > 180):
    d = d - 360
  elif (d <= -180):
    d = 360 + d
  return d


def sign(x):
    return (0 if x == 0 else (
                -1 if x < 0 else 1))


def longestCommonSubsequence(array1, array2, opt_compareFn, opt_collectorFn):
  
  compare = opt_compareFn or (lambda a, b: a == b)
  collect = opt_collectorFn or (lambda i1, i2: array1[i1])
  
  length1 = array1.length;
  length2 = array2.length;
  
  arr = [];
  for i in range(length1 + 1):
    arr[i] = []
    arr[i][0] = 0
  
  for j in range(length2 + 1):
    arr[0][j] = 0
  
  for i in range(1, length1 + 1):
    for j in range(1, length1 + 1):
      if compare(array1[i - 1], array2[j - 1]):
        arr[i][j] = arr[i - 1][j - 1] + 1
      else:
        arr[i][j] = Math.max(arr[i - 1][j], arr[i][j - 1])
  
  # Backtracking
  result = [];
  i = length1
  j = length2
  while i > 0 and j > 0:
    if compare(array1[i - 1], array2[j - 1]):
      result.unshift(collect(i - 1, j - 1))
      i -= 1
      j -= 1
    else:
      if arr[i - 1][j] > arr[i][j - 1]:
        i -= 1
      else:
        j -= 1
  
  return result


def sum(var_args):
  return reduce(
              arguments,
              lambda sum, value: sum + value,
              0)


def average(var_args):
  return sum.apply(None, arguments) / arguments.length


def standardDeviation(var_args):
  
  sampleSize = arguments.length
  if sampleSize < 2:
    return 0
  
  mean = average.apply(None, arguments)
  
  variance = (
                sum.apply(
                    None,
                    map(
                        arguments,
                        lambda val: Math.pow(val - mean, 2))) /
                (sampleSize - 1))
  
  return Math.sqrt(variance)


def isInt(num):
  return isFinite(num) and num % 1 == 0


def isFiniteNumber(num):
  return isFinite(num) and not isNaN(num)


