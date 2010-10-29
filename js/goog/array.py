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

