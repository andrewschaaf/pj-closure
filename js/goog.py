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


#TODO explore what this should be in a (function(){...})() world
goog.global_ = window;



def bind(fn, selfObj, var_args):
  
  context = selfObj or goog.global_
  
  if len(arguments) > 2:
    boundArgs = Array.prototype.slice.call(arguments, 2)
    
    def bound():
      # Prepend the bound arguments to the current arguments.
      newArgs = Array.prototype.slice.call(arguments);
      Array.prototype.unshift.apply(newArgs, boundArgs);
      return fn.apply(context, newArgs);
    
    return bound
  
  else:
    return lambda: fn.apply(context, arguments)


def isString(val):
  return typeof(val) == 'string'

