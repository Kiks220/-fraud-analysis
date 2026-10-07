[🇷🇺 Русская версия](README.md)
# Double Game: How Fraudsters Exploit Tragedy and a "Rescuer" for a Second Attack

## Introduction

In my practice, I encountered a case that goes beyond typical social engineering schemes. Fraudsters used a family tragedy as the **first stage of the attack**, and after failure, returned posing as law enforcement officers — this time as "rescuers." Below is an analysis of this two-stage scheme.

## Context

- **Victim:** mother of a deceased serviceman.
- **Trigger:** grief, shock, vulnerability.
- **First contact:** a call reporting the death of her son. They offer to "send documents" for the delivery of the body or photos of the deceased — so the mother can identify the body.
- **Goal:** trick the victim into sharing personal data or opening a malicious file/link.

## Stage 1: "Death Notification"

- **Legend:** "Your son has died. We need your assistance as his mother."
- **Psychological pressure:** exploiting grief, shock, the desire to see "documents."
- **Technical mechanics:** file or link (phishing or malware).
- **Failure:** the victim recognized the fraudster and prolonged the conversation.
- **Fraudster's mistake:** he didn't mute the microphone and told his colleague: "We almost got her." The victim heard and hung up.

## Stage 2: "The Rescuer"

- **New call:** poses as a law enforcement officer.
- **Legend:** "I tracked that scammers called you. They are already stealing your personal data. We need to act urgently."
- **Goal:** regain trust, gain access to data or money.
- **Why it works:** the victim is already scared, and the "rescuer" appears as the only ally.

## Psychological Analysis

- **Why grief is used:** in a state of shock, a person loses critical thinking.
- **Why the "rescuer" works:** after stress, the victim seeks protection.
- **Why the fraudster slipped up:** human factor, underestimating the victim.

## Technical Traces

- IP addresses of calls (if available).
- Phone numbers (anonymized).
- Links/files they tried to send.
- Call times (for provider request).

## How It Is Investigated

- Request to the provider: NAT logs, MAC address.
- Request to the bank: if there were transactions.
- Analysis of links/files (if the victim opened them).
- Search for connections between the first and second calls (same IP? same number?).

## Conclusions and Recommendations

- A real law enforcement officer **never** asks for codes or money transfers over the phone.
- If necessary, the officer will ask you to come to the station or will come themselves.
- If the victim has already opened a file or clicked a link — urgently block bank cards and contact the police.

## Disclaimer

> All data is anonymized. The scheme is described for educational purposes. It is not a call to action.
