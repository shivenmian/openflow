

Hey Arneish,

Wanted to reach out to schedule our next product sync. Have a few topics in mind:
- user supportability
- security contraints
- our next business trip to Arizona

Let me know a good time.

Thanks,
Shiven


Hey Akash, was wondering if you had any thoughts on the upcoming product launch with the new features: revamped UX, new encryption, and new hardware enhancements. Thanks, Shiven



------
So we've noticed some existing products that take in speech and output structured text.
As people with less traditional names, our names are often mispelled by vanilla speech transcription models.

pipeline:
- whisper (locally) to transcribe
- OCR to identify entities from chat and email UI - tessaract
- local vector DB to save contact info
- GPT-4o for entity replacement
- pyperclip for pasting the text in



