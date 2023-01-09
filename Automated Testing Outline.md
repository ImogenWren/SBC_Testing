# Automated Testing


The ideal scenario is an additional SBC to act as the test coordinator. This can run the testPing.py (or similar) script and send and email if an offline host is detected.

- If Test Coordinator is powered from the same power supply it should only run script when all hosts should also be alive
- Emailing is the ideal situation, however requires internet access, so as a workaround it will simply log to file each host that is down and for how long 
  - Goal 1: Log Host down time during every test then manually calculate down time
  
