# FCP Gym

FC Portugal 3D gym environment to train a kick in motion for the RoboCup 3D Simulation League.

It uses OpenAI [Gym](https://gym.openai.com/docs/) under the hood, so the API is the same.

To run the environment with randomly sampled actions:

```python
import fcpgym as gym

env = gym.make('KickInMotion', host="localhost", agent_port=3100, monitor_port=3200)
for _ in range(10):
	obs = env.reset()
	done = False
	while not done:
		action = env.action_space.sample()
		obs, reward, done, info = env.step(action)
env.close()
```

# Preview

[![](https://i.imgur.com/f0MaVfC.png)](https://youtu.be/MFrtjojuZAg)

# Kick in motion

```cpp
/**
 * The agent walks towards the ball and should learn to kick it while moving.
 * 
 * Model: Nao Robot (type 4)
 * 
 * Actions: Box(20)
 *     #       Description                         Min              Max
 *     ----    --------------------------------    -------------    ------------
 *     0-19    Joint angular velocity (rad/sec)    -6.1395447097    6.1395447097
 * 
 * Observations: Box(67)
 *     #        Description                            Min             Max
 *     -----    -----------------------------------    ------------    ------------
 *     0-2      Ball position relative to torso (m)    -INFINITY       INFINITY
 *     3-26     Joint angle (deg)                      -INFINITY       INFINITY
 *     27-29    Torso angular velocity (deg/sec)       -INFINITY       INFINITY
 *     30-32    Torso proper acceleration (m^2/sec)    -INFINITY       INFINITY
 *     33-65    Derivatives of all of the above        -INFINITY       INFINITY
 *     66       Episode elapsed time (sec)             -INFINITY       INFINITY
 * 
 * Info: Empty.
 * 
 * Reward: Distance the ball moved in the desired kick path.
 *         Calculated by projecting the current ball position on the desired kick path.
 *         Range: [-INFINITY, INFINITY].
 * 
 * Episode Start: Robot is close enough to kick the ball.
 * 
 * Episode End: Ball stops after being kicked,
 *              or episode takes too long,
 *              or robot falls.
 */
```

# Operating System

[Ubuntu 18](http://releases.ubuntu.com/18.04/).

# Server

1. Install dependencies:

    ```bash
    sudo apt-get install g++ git cmake libfreetype6-dev libode-dev libsdl-dev ruby ruby-dev libdevil-dev libboost-dev libboost-thread-dev libboost-regex-dev libboost-system-dev qt4-default
    ```

2. Download the SimSpark repository:

    ```bash
    git clone https://gitlab.com/robocup-sim/SimSpark.git
    ```

3. Build and install:

    ```bash
    cd SimSpark
    sudo ./build.sh
    ```

4. Change the following settings:

    ```bash
    /usr/local/share/rcssserver3d/rcssserver3d.rb
        $enableRealTimeMode = false
    /usr/local/share/rcssserver3d/naosoccersim.rb
        addSoccerVar('BeamNoiseXY',0.0)
        addSoccerVar('BeamNoiseAngle',0.0)
        #gameControlServer.initControlAspect('SoccerRuleAspect')
    /usr/local/share/rcssserver3d/rsg/agent/nao/naoneckhead.rsg
        (setViewCones 120 120) ; 
        (setSenseMyPos true) ;
        (setSenseMyOrien true) 
        (setSenseBallPos true) ; 
        (addNoise true)
    ~/.simspark/spark.rb
        $agentSyncMode = true
    ```

# Viewer

1. Install dependencies:

    ```bash
    sudo apt install openjdk-8-jdk
    ```

2. Download the RoboViz repository:

    ```bash
    git clone https://github.com/magmaOffenburg/RoboViz.git
    ```

3. Build and install:

    ```bash
    cd RoboViz/scripts
    ./build.sh
    echo "alias roboviz='$PWD/../bin/roboviz.sh'" >> ~/.bash_aliases
    ```

4. Open the viewer:

    ```bash
    roboviz
    ```

# FCP Gym

1. Install dependencies:

    ```bash
    sudo apt install libboost-dev libboost-regex-dev libicu-dev libboost-system-dev libboost-program-options-dev libboost-thread-dev zlib1g-dev ruby ruby-dev libfreetype6-dev libode-dev g++ subversion cmake libsdl-dev libdevil-dev qt4-default libgtk2.0-dev libxml2-dev liblua5.1-0-dev libboost-filesystem-dev libgsl-dev python3-dev
    ```

2. Run the example:

    ```bash
    python3 example.py
    ```
