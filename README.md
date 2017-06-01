# TOC Project 2017

Template Code for TOC Project 2017

A telegram bot based on a finite state machine

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip3 install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
./ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `start`.

Every time each state is triggered to `advance` to another state.
After the input is "我要走了" , no matter which state is , it will `advance` to `end` state , and the `end` state will `go_back` to `start` state 

* start
	* Input: "你好"
		* go to `user`
		* Reply: "你好～我是QQ ......[療癒][搞笑][負能量][正能量]"

* user
	* Input: "療癒"
		* go to `state1`
		* Reply: "....[動物][植物][都不要]"

	* Input: "搞笑"
		* go to `state2`
		* Reply: "....[笑話][影片][其他][都不要]"
		
	* Input: "負能量"
		* go to `state3`
		* Reply: "....[粉絲專頁][其他][都不要]"

	* Input: "正能量"
		* go to `state4`
		* Reply: "....[經典][溫暖][都不要]"

* state1
	* Input: "動物"
		* go to `state11`
		* Reply: "....[狗][貓][其他][不要了]"

	* Input: "植物"
		* go to `state12`
		* Reply: "....[花][草][不要了]"
		
	* Input: "都不要"
		* go to `user`
		* Reply: "你好～我是QQ ......[療癒][搞笑][負能量][正能量]"

* state2
	* Input: "笑話"
		* go to `state21`
		* Reply: "....[嘿嘿嘿][funny][換別的]"

	* Input: "影片"
		* go to `state22`
		* Reply: "....[豆豆先生][這群人][監獄兔][換別的]"
		
	* Input: "其他"
		* go to `state23`
		* Reply: "....[進來看看][換別的]"

	* Input: "都不要"
		* go to `user`
		* Reply: "你好～我是QQ ......[療癒][搞笑][負能量][正能量]"
		
* state3
	* Input: "粉絲專頁"
		* go to `state31`
		* Reply: "....[厭世動物園][厭世哲學家][來點負能量][夠了]"
		
	* Input: "其他"
		* go to `state32`
		* Reply: "....[進來看看][夠了]"

	* Input: "都不要"
		* go to `user`
		* Reply: "你好～我是QQ ......[療癒][搞笑][負能量][正能量]"

* state4
	* Input: "經典"
		* go to `state41`
		* Reply: "....[厭世動物園][厭世哲學家][來點負能量][不用了]"
		
	* Input: "溫暖"
		* go to `state42`
		* Reply: "....[溫暖1][溫暖2][不用了]"

	* Input: "都不要"
		* go to `user`
		* Reply: "你好～我是QQ ......[療癒][搞笑][負能量][正能量]"

* state11
	* Input: "狗"
		* go to `state111`
		* Reply: "...."

	* Input: "貓"
		* go to `state112`
		* Reply: "...."

	* Input: "其他"
		* go to `state113`
		* Reply: "...."

	* Input: "不要了"
		* go to `state1`
		* Reply: "[動物][植物][都不要]"

* state12
	* Input: "花"
		* go to `state121`
		* Reply: "...."

	* Input: "草"
		* go to `state122`
		* Reply: "...."
		
	* Input: "不要了"
		* go to `state1`
		* Reply: "[動物][植物][都不要]"
		
* state21
	* Input: "嘿嘿嘿"
		* go to `state211`
		* Reply: "...."
		
	* Input: "funny"
		* go to `state212`
		* Reply: "...."

	* Input: "換別的"
		* go to `state2`
		* Reply: "[笑話][影片][其他][都不要]"

* state22
	* Input: "豆豆先生"
		* go to `state221`
		* Reply: "...."
		
	* Input: "這群人"
		* go to `state222`
		* Reply: "...."

	* Input: "監獄兔"
		* go to `state223`
		* Reply: "...."
		
	* Input: "換別的"
		* go to `state2`
		* Reply: "[笑話][影片][其他][都不要]"
* state23
	* Input: "進來看看"
		* go to `state231`
		* Reply: "...."

	* Input: "換別的"
		* go to `state2`
		* Reply: "[笑話][影片][其他][都不要]"
		
* state31
	* Input: "厭世動物園"
		* go to `state311`
		* Reply: "...."
		
	* Input: "厭世哲學家"
		* go to `state312`
		* Reply: "...."

	* Input: "來點負能量"
		* go to `state313`
		* Reply: "....]"
		
	* Input: "夠了"
		* go to `state3`
		* Reply: "[粉絲專頁][其他][都不要]"
		
* state32
	* Input: "進來看看"
		* go to `state321`
		* Reply: "...."
		
	* Input: "夠了"
		* go to `state3`
		* Reply: "[粉絲專頁][其他][都不要]"

* state41
	* Input: "經典1"
		* go to `state411`
		* Reply: "...."
		
	* Input: "經典2"
		* go to `state412`
		* Reply: "...."
	
	* Input: "經典3"
		* go to `state413`
		* Reply: "...."

	* Input: "不用了"
		* go to `user`
		* Reply: "[經典][溫暖][都不要]"

* state42
	* Input: "溫暖1"
		* go to `state421`
		* Reply: "...."
		
	* Input: "溫暖2"
		* go to `state422`
		* Reply: "...."

	* Input: "不用了"
		* go to `user`
		* Reply: "[經典][溫暖][都不要]"
		
## Author
[Lee-W](https://github.com/Lee-W) [F74036239]
