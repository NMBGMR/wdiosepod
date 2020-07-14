/**
 * Copyright 2018, Google LLC
 * Licensed under the Apache License, Version 2.0 (the `License`);
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an `AS IS` BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
'use strict';
var box_div, message, log, log_div;

window.addEventListener('load', function () {
  console.log("window loaded");
  box_div = document.getElementById('message_box');
  log_div = document.getElementById('log_box');

  // create a new <p> element and store it in 'el'
  message = document.createElement('p');
  log = document.createElement('p');

  // add text to the new <p> element
  message.appendChild(document.createTextNode(""));
  log.appendChild(document.createTextNode(""));

  // append the new <p> element to the div
  box_div.appendChild(message);
  log_div.appendChild(log);

});


const update = async () => {
  console.log('doing periodic')
  const response = await fetch('/status');
  const resp = await response.json(); //extract JSON from the http response
  console.log(resp)
  message.innerHTML = resp['message']
  log.innerHTML = resp['log']

  // do something with myJson
}

var intervalID = setInterval(update, 5000);
