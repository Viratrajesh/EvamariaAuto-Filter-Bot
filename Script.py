import os
class script(object):

    START_TXT = """<b><i>Hi {},

I am a powerful auto-filter bot with advanced feature.
You can use me in your group, I will give any movies, series or anime in group...

<code>{}</code></i></b>"""

    HELP_TXT = """<b><i>Click on the below buttons to get documentation about specific modules..</i></b>"""

    CODEXBOTS = """<b><i>/upload - send me picture or video under (5MB)

Note - this command only works in PM</i></b>"""

    STATUS_TXT = """<b><u>🗃 Database 1 🗃</u>

» Total users - <code>{}</code>
» Total groups - <code>{}</code>
» Used storage - <code>{} / {}</code>

<u>🗳 Database 2 🗳</u></b>

» Total files - <code>{}</code>
» Used storage - <code>{} / {}</code>

<b>🤖 Bot details 🤖</b>

» Uptime - <code>{}</code>
» RAM - <code>{}%</code>
» CPU - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#New_User

≈ ID:- <code>{}</code>
≈ Name:- {}</b>"""

    NEW_GROUP_TXT = """#New_Group

Group name - {}
ID - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    IMDB_TEMPLATE_TXT = """<b>📻 Title - <a href={url}>{title}</a>
🎭 Genres - {genres}
🎖 Rating - <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user rating.)
📆 Year - {release_date}
❗️ Language - {languages}</b>
"""

    FILE_CAPTION = """<b><a href=https://t.me/+LO--J2nVD3syYzBl>{file_name}</a></b>

<i>Please forward these files to the Saved Messages \nIts Deleted within 10mins</i>"""

    RESTART_TXT = """<b>
📅 Date : <code>{}</code>
⏰ Time : <code>{}</code>
🌐 Timezone : <code>Asia/Kolkata</code></b>"""

    ALRT_TXT = """❌ That is not for you, sir ⛔️"""

    OLD_ALRT_TXT = """You are using one of my old messages, please send the request again"""

    NO_RESULT_TXT = """🗳 This movie is not yet released or added to database 🗳"""

    I_CUDNT = """🤧 Hello {}

I couldn't find any movie or series in that name.. 😐"""

    I_CUD_NT = """😑 Hello {}

I couldn't find anything related to that 😞... check your spelling."""

    CUDNT_FND = """🤧 Hello {}

I couldn't find anything related to that. Did you mean one of these?? 👇"""

    FONT_TXT = """<b><i>You can use this mode to change your font style.</i></b>

<code>/font hi how are you</code>"""

    PREMIUM_TEXT = """<b><i><blockquote>Available plans ♻️</blockquote>

• 1 week  - ₹15
• 1 month  - ₹39
• 3 months  - ₹99
• 6 months  - ₹149
• 1 year  - ₹199

•─────•─────────•─────•
<blockquote>Premium features 🎁</blockquote>

○ No need to verify
○ Direct files
○ Ad-free experience
○ Unlimited movies, series & anime
○ Full admin support
○ Request will be completed in 1h
•─────•─────────•─────•

✨ UPI ID - <code>yuxe@ybl</code>

Check your active plan with /myplan

💢 Must send screenshot after payment

‼️ After sending a screenshot please give me some time to add you in the premium version.</i></b>"""

    VERIFICATION_TEXT = """<b>Hi {} {},

You are not verified today 😐
Click on verify and get unlimited access till next verification

#Verification:- 1/3

<blockquote>If you want direct files then you can take premium service. (no need to verify)</blockquote>

Check /plan for more details...</b>"""

    VERIFY_COMPLETE_TEXT = """<b>Hi {},

You have completed the 1st verification...

Now you have unlimited access till next verification ❤️‍🔥

If you want direct files without any verifications then buy our subscription 😁

💶 Check /plan to buy subscription</b>"""

    SECOND_VERIFICATION_TEXT = """<b>Hi {} {},

You are not verified today 😐
Click on verify and get unlimited access till next verification

#Verification:- 2/3

<blockquote>If you want direct files then you can take premium service. (no need to verify)</blockquote>

Check /plan for more details...</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>Hi {},

You have completed the 2nd verification...

Now you have unlimited access till next verification ❤️‍🔥

If you want direct files without any verifications then buy our subscription 😁

💶 Check /plan to buy subscription</b>"""

    THIRDT_VERIFICATION_TEXT = """<b>Hi {} {},

You are not verified ‼️
Tap on the verify link and get unlimited access for today 😇

#Verification:- 3/3

<blockquote>If you want direct files then you can take premium service. (no need to verify)</blockquote>

Check /plan for more details...</b>"""

    THIRDT_VERIFY_COMPLETE_TEXT = """<b>Hi {},

You are now verified for today ☺️

Enjoy unlimited movies, series or anime 💥

If you want direct files without any verifications then buy our subscription 😁

💶 Check /plan to buy subscription</b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ User verified successfully ☄</u>

⚡️ Name:- {} [ <code>{}</code> ] 
📆 Date:- <code>{}</code></b>

#verification_{}_completed"""

    CUSTOM_TEXT = """<b><i>😊 <u>Your group all commands</u> 😊

/shortlink - to set shortener
/shortlink2 - to set shortener for 2nd verify
/shortlink3 - to set shortener for 3rd verify
/time2 - to set 2nd shortener verify time
/time3 - to set 3rd shortener verify time
/log - to set log channel for users data
/tutorial - to set 1st tutorial video link
/tutorial2 - to set 2nd tutorial video link
/tutorial3 - to set 3rd tutorial video link
/caption - to set custom file caption
/template - to set custom imdb template
/fsub - to set your force subscribe channel
/nofsub - to remove force sub channel
/ginfo - to check your group details</i></b>

😘 If you do all this then your group will be very cool..."""

    FSUB_TXT = """{},

<i><b>🙁 First join our channel then you will get movie, otherwise you will not get it.

Click join now button 👇</b></i>"""

    DONATE_TXT = """<blockquote>❤️‍🔥 Thanks for showing interest in Donation</blockquote>"""

DONATE_TXT = """<b><i>💞 If you like our bot feel free to donate any amount ₹10, ₹20, ₹50, ₹100, etc.</i></b>

❣️ UPI ID : <code>yuxe@ybl</code>"""
