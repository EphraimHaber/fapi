# fapi
this POC project uses fast-api which is not installed on my local machine. 
I will config pycharm to use a remote interpreter from the container.

Let's go step by step:
1. Open a terminal in the fapi directory.
2. run
   ```docker compose up --build -d ``` 
<img width="269" alt="image" src="https://github.com/EphraimHaber/fapi/assets/61934858/510464d8-aec7-4379-8b32-06dfccc5150e">

3. Note that this doesn't give us autocomplete. Even though the code runs and reacts to changes in the file, that is because of the volume defined in the dokcer-compose.yaml file
4. Click `ctrl`+`shift`+`s`
5. Go to the project python interpreter
6. On the top right corner of the screen click `Add Interpreter` > `On Docker compose`
7. <img width="309" alt="image" src="https://github.com/EphraimHaber/fapi/assets/61934858/e2e94255-07e8-4b1b-b95e-1b2da8587237">
9. Clicl `Apply` > `Ok`
8. Click `Next` > `Next` > `Create`
### Note that in order for this to connect we will need the BusyBox image.
https://hub.docker.com/_/busybox

9* You will need to transfer that image to your air gapped network if you are using one. the following line is the relevent line when I run `docker images` on my host machine

    busybox            latest            a416a98b71e2   2 weeks ago      4.26MB

10. This will build (now offline) another image pycharm_helpers (and spin a container of course)
11. You now have intellisense from the IDE.
12. In order to debug we will need to make a debug run config
    <img width="492" alt="image" src="https://github.com/EphraimHaber/fapi/assets/61934858/f314de67-2874-46d3-b670-078633d199d9">
13. Click on the green triangle and then on `Debug main`
    
    <img width="487" alt="image" src="https://github.com/EphraimHaber/fapi/assets/61934858/7b38c0c1-50be-47cd-af5b-0e1d5d4ae6f6">
14. This should make a run config. In case you need here is the one I made.
<img width="774" alt="image" src="https://github.com/EphraimHaber/fapi/assets/61934858/ec14d50d-ed4f-4690-a90f-b2b9ec294fed">

15. I've put a breakpoint on line 10 and then retried to load `http://localhost:8000/`
    
    <img width="422" alt="image" src="https://github.com/EphraimHaber/fapi/assets/61934858/d8c752a4-074c-4000-a8fe-29d5ff8eedcf">

## And that's it. Good luck!.





