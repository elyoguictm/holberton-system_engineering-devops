
# 0x19-Postmortem

#### As a cybersecurity manager, I dare to say that we are not powerful at all, they (cybercriminals) have better technologies and are always one step ahead of us, this is something that i understood that 28/02/18..
#### Today I will tell you a story of when a ransomware took us by surprise 

<img align="right" alt="jpg" src="https://i.imgflip.com/37m3pe.jpg" width="400" height="300" />


#### What the @%uk is happening!?
###### It was a working Wednesday like any other, working for a bank, I was the cybersecurity manager, with a team of 2 people, me and Maria, she is a cybersecurity trainee.
###### Since we were always relaxed, we didn't have much to do.
###### Who would attack a bank?
###### Well that day we didn't have the same luck
###### That Wednesday my partner Maria calls me from her desk
###### Maria - Hey, Gabriel .. I have a little problem ..
###### Me - Yes, what happens?
###### Maria - Well, my files won't open .. I think I did something wrong ..
###### Me - Let me see .. hmm try rebooting, maybe it was a simple glitch in the operating system!
##### *5 minutes later*
###### Maria comes to my desk again, but this time she was scared ..
###### Maria - Gabriel ..
#####  * That's my phone ringing * It was the executive director !!
###### Richard - What the hell is going on !? My computer has an alert that the files are encrypted and that i must pay a ransom.
###### Maria - Just that I came to tell you ..
###### This can't be happening.. a ransomware???
<img align="center" alt="jpg" src="https://www.freeitdata.com/wp-content/uploads/2020/01/watermark_newsletter_cybercrime-680x423.jpg" width="800" height="400" />

### Summary
| Incident Summary   |        |
|--------------------|--------|
| Incident Number    |  0015  |
| Postmortem Date    |28/02/18|
| Incident Severity  |  10/10 |

### Incident Timing
| Start Time      |  Date/Time                   | Incident Detected By (User-reported)                                    |
|-----------------|------------------------------|-------------------------------------------------------------------------|
| Detection Time  |  08:30 Montevideo/Uruguay    | Maria (Cybersecurity Trainee)                                           |
| Resolution Time |  22:45 Montevideo/Uruguay    | Gabriel (Cybersecurity Manager)                                         |

### Incident Timeline
| Date/Time | Who/What         | Action/ Impact                             |
|-----------|------------------|--------------------------------------------|
|  08:30    | Cyberattacker    | Files won't open/Infection                 |
|  08:35    | Cyberattacker    | Data hijacking                             |
|  09:00    | Gabriel          | Scanning                                   |
|  09:50    | Gabriel          | Looking for solutions to the problem       |
|  17:10    | Richard          | Try to pay ransom                          |
|  20:13    | Gabriel          | Find some bugs in the attack               |
|  20:39    | Gabriel          | The backups are being restored             |
|  20:39    | Gabriel          | The restoration of the backups is finished |
|  22:45    | Team             | We won the battle                          |

### Impact

##### The bank had to stop operating for almost 15 hours, that means several angry customers, the press talking about our security sucks .. I stink, I was responsible for this ..
##### Although it was only 2 computers that were infected, I feared the worst, could they infect the others?
##### I got up, took my laptop and got to work, I was not going to let him do this to us.
##### I even lead Richard, our director, to try to pay the ransom

### End User Impact
##### We lost several users as they mistrusted our security and our service, my boss wanted to kill me 


### What caused the incident?

##### Although it may seem strange to you that a cybersecurity employee, María, opened a malicious email, which infected those 2 computers.
##### She was a Trainee, that was my fault, I should have instructed her better, although anyone knows that opening an email from a company that no one knows and that her email  ends in .ru is not trustworthy.

### Root Cause(s)

|  Causes                              | Percent          | Action                                                         |
|--------------------------------------|------------------|----------------------------------------------------------------|
|  Spam/phishing emails                | 76%              | Use an AI that detects malicious emails                        |
|  Poor user practices/employee        | 19%              | We create workshops for our users to learn about these threats |
|  Weak passwords/access management    | 5%               | Now we access with cards                                       |

### Mitigation & Resolution
##### As I was always someone very paranoid, I had an ace up my sleeve
##### Backups! Yes, there were several a week so these were quite up-to-date, it took us a while to restore everything but over time we succeeded.


#### Lessons Learnt
##### Do not leave such important data to a trainee.. (sorry Maria)
##### Encrypt emails and train our customers and employees to avoid these attacks.
##### Backups can literally save your life and your company.
##### Never underestimate that by working in a bank with a team in charge of cybersecurity you will be powerful, on the contrary, you are the target of thousands of attackers.
##### A small error in the network configuration can be a disaster. 
 

### What went well
##### The ransomware, although I do not want to underestimate it since it is one thing to speak now and another what we live.
##### It was not at all powerful, it had several errors that we could use to our advantage.
##### This omitted to encrypt some files in which we store information of our clients .
##### And obviously what i'm proud of, my backup. <3

### What went badly
##### Something that I feel guilty of is not educating my trainee correctly about these things, believing it obvious made her fall for an old trick.
##### and believe us invincible ..

### That was my story, but like this there are many. We must educate ourselves about this and not fall into traps that can cost us millions. 

<p align="center">
  <img alt="GIF" src="https://i.pinimg.com/originals/0f/ab/3e/0fab3e4f7e9e7d3f199c49f10308ac05.gif" width="800" height="400" />
</p>
