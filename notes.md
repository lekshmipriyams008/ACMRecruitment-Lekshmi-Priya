Navigated to ~/Downloads and listed files with ls -la to locate BLOCKCHAIN-CHALLENGE.zip.
Unzipped it with unzip -o, then cd'd into the extracted folder and listed contents again.
Read README.md for the challenge story/context.
Used grep -n to locate the burn address 0x000...dEaD inside transactions.json.
Used -A 10 -B 2 to grab surrounding lines and expose the hidden input field.
Extracted the hex string from "input" and piped it through xxd -r -p to decode hex → ASCII, revealing the flag: CTF{0n_ch41n_gr4ff1t1_1sn7_pr1v4t3}
