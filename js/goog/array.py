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


# TODO the rest

from goog import bind, isString


ARRAY_PROTOTYPE_ = Array.prototype


def concat(var_args):
  return ARRAY_PROTOTYPE_.concat.apply(ARRAY_PROTOTYPE_, arguments)


def forEach(arr, f, opt_obj):
  #DIFF: goog runs this if-statement at load-time
  
  if ARRAY_PROTOTYPE_.forEach:
    # TODO assert(arr.length != None)
    ARRAY_PROTOTYPE_.forEach.call(arr, f, opt_obj)
  
  else:
    arr2 = (arr.split('') if isString(arr) else arr)
    for i in range(len(arr)):
      if i in arr2:
        f.call(opt_obj, arr2[i], i, arr)


def map(arr, f, opt_obj):
  #DIFF: goog runs this if-statement at load-time
  
  if ARRAY_PROTOTYPE_.map:
    #TODO goog.asserts.assert(arr.length != null);
    return ARRAY_PROTOTYPE_.map.call(arr, f, opt_obj)
  
  else:
    l = len(arr)
    res = Array(l)
    arr2 = (arr.split('') if isString(arr) else arr)
    for i in range(l):
      if i in arr2:
        res[i] = f.call(opt_obj, arr2[i], i, arr)
      return res


def reduce(arr, f, val, opt_obj):
  
  if arr.reduce:
    if opt_obj:
      return arr.reduce(bind(f, opt_obj), val)
    else:
      return arr.reduce(f, val)
  
  rval = val
  
  def f(val, index):
    rval = f.call(opt_obj, rval, val, index, arr)
  
  forEach(arr, f)
  
  return rval


def slice(arr, start, opt_end):
  #goog.asserts.assert(arr.length != null);
  
  # passing 1 arg to slice is not the same as passing 2 where the second is
  # null or undefined (in that case the second argument is treated as 0).
  # we could use slice on the arguments object and then use apply instead of
  # testing the length
  if arguments.length <= 2:
    return ARRAY_PROTOTYPE_.slice.call(arr, start)
  else:
    return ARRAY_PROTOTYPE_.slice.call(arr, start, opt_end)


def splice(arr, index, howMany, var_args):
  #goog.asserts.assert(arr.length != null)
  return ARRAY_PROTOTYPE_.splice.apply(
      arr, slice(arguments, 1))



def insertAt(arr, obj, opt_i):
  splice(arr, opt_i, 0, obj)



def filter(arr, f, opt_obj):
  if ARRAY_PROTOTYPE_.filter:
    #goog.asserts.assert(arr.length != null);
    return ARRAY_PROTOTYPE_.filter.call(arr, f, opt_obj)
  else:
    res = []
    resLength = 0
    arr2 = arr.split('') if isString(arr) else arr
    for i in range(len(arr)):
      if i in arr2:
        val = arr2[i]
        if f.call(opt_obj, val, i, arr):
          # Is this better than .push?
          resLength += 1
          res[resLength] = val
    return res


def indexOf(arr, obj, opt_fromIndex):
  if ARRAY_PROTOTYPE_.indexOf:
    #goog.asserts.assert(arr.length != null);
    return ARRAY_PROTOTYPE_.indexOf.call(arr, obj, opt_fromIndex)
  else:
    
    fromIndex = (
                  0
                  if opt_fromIndex == None else
                  (
                    Math.max(0, arr.length + opt_fromIndex)
                    if opt_fromIndex < 0 else
                    opt_fromIndex))
    
    if isString(arr):
      # Array.prototype.indexOf uses === so only strings should be found.
      if not isString(obj) or len(obj) != 1:
        return -1
      return arr.indexOf(obj, fromIndex)
    
    for i in range(fromIndex, len(arr)):
      if (i in arr) and (arr[i] == obj):
        return i
    
    return -1


