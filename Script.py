import os
class script(object):

START_TXT = """<b><i>Hey {} {},

I'm a powerful auto filter bot with an advanced earning feature.
You can use me in your group to get any movies, series, or anime using your connected shortener.

Your ID - <code>{}</code></i></b>"""

HELP_TXT = """<b><i>Click the buttons below to get help about each feature.</i></b>"""

CODEXBOTS = """<b><i>/upload - Send me a photo or video under 5MB

Note - This works only in private chat.</i></b>"""

STATUS_TXT = """<b><u>🗃 Database 1 🗃</u>

» Total Users - <code>{}</code>
» Total Groups - <code>{}</code>
» Used Storage - <code>{} / {}</code>

<u>🗳 Database 2 🗳</u></b>

» Total Files - <code>{}</code>
» Used Storage - <code>{} / {}</code>

<u>🤖 Bot Details 🤖</u>

» Uptime - <code>{}</code>
» RAM - <code>{}%</code>
» CPU - <code>{}%</code></b>"""

NEW_USER_TXT = """<b>#New_User

≈ ID:- <code>{}</code>
≈ Name:- {}</b>"""

NEW_GROUP_TXT = """#New_Group

Group Name - {}
ID - <code>{}</code>
Username - @{}
Link - {}
Members - <code>{}</code>
Added By - {}"""

IMDB_TEMPLATE_TXT = """<b>📻 Title - <a href={url}>{title}</a>

🎭 Genres - {genres}
🎖 Rating - <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user votes)
📆 Year - {release_date}
❗️ Language - {languages}</b>"""

FILE_CAPTION = """<b><a href=https://telegram.me/Askmovies4>{file_name} </a></b>

<i>Please forward this file to Saved Messages and close this message.</i>"""

RESTART_TXT = """<b>

📅 Date : <code>{}</code>
⏰ Time : <code>{}</code>
🌐 Timezone : <code>Asia/Kolkata</code></b>"""

ALRT_TXT = """❌ That option is not for you ⛔️"""

OLD_ALRT_TXT = """You are using an old message, please send the request again."""

NO_RESULT_TXT = """🗳 This movie is not yet released or not in our database 🗳"""

I_CUDNT = """🤧 Hello {}

I couldn’t find any movie or series by that name... 😐"""

I_CUD_NT = """😑 Hello {}

I couldn’t find anything by that name 😞... Please check your spelling."""

CUDNT_FND = """🤧 Hello {}

I couldn’t find anything with that name. Did you mean one of these? 👇"""

FONT_TXT = """<b><i>You can use this to change your font style.</i></b>

<code>/font hi how are you</code>"""

PREMIUM_TEXT = """<b><i><blockquote>Available Plans ♻️</blockquote>

🎁 Premium Plans 🎁

☆ 1 Week - ₹15
☆ 1 Month - ₹39
☆ 3 Months - ₹99
☆ 6 Months - ₹129

•─────•─────────•─────•

<blockquote>  🎁</blockquote>  
🎁 Premium Features 🎁  
○ No need to verify
○ No need to open links
○ Direct files
○ Ad-free experience
•─────•─────────•─────•

✨ UPI ID - <code>Rajesh1162005@oksbi</code>

Check your active plan using /myplan

💢 Send screenshot after payment

‼️ After sending, give me some time to activate your premium.</i></b>"""

EARN_TEXT = """<b><i><blockquote>How to earn money using this bot 🤑</blockquote>

›› Step 1: Have a group with at least 300 members.

›› Step 2: Make <a href=https://telegram.me/{}</a> an admin in your group.

›› Step 3: Create account on <a href='https://tnshort.net/ref/devilofficial'>TNLink</a> or <a href='https://onepagelink.in/ref/Nobita'>OnePageLink</a>. (You can use other shorteners too)

›› Step 4: Set your shortener, tutorial, fsub, and log channel.

›› Step 5: Follow these <a href='https://github.com/blob/main/README.md'>instructions</a>.

Check your values using /ginfo command.

💯 Note - This bot is free to use. You can earn unlimited money using it in your group.</i></b>"""

VERIFICATION_TEXT = """<b>Hey {} {},

You're not verified today 😐
Click Verify to unlock access until next verification.

#Verification:- 1/3

<blockquote>Want direct files? Buy premium and skip verification.</blockquote> 
Check /plan for more info.</b>"""

VERIFY_COMPLETE_TEXT = """<b>Hey {},

You have completed the 1st verification.

You now have unlimited access until the next one ❤️‍🔥

Want direct files without verifications? Buy our subscription 😁

💶 Check /plan to buy it.</b>"""

SECOND_VERIFICATION_TEXT = """<b>Hey {} {},

You're not verified today 😐
Click Verify to unlock access until next verification.

#Verification:- 2/3

<blockquote>Want direct files? Buy premium and skip verification.</blockquote> 
Check /plan for more info.</b>"""

SECOND_VERIFY_COMPLETE_TEXT = """<b>Hey {},

You have completed the 2nd verification.

You now have unlimited access until the next one ❤️‍🔥

Want direct files without verifications? Buy our subscription 😁

💶 Check /plan to buy it.</b>"""

THIRDT_VERIFICATION_TEXT = """<b>Hey {} {},

You're not verified ❗️
Click Verify to get full access for today 😇

#Verification:- 3/3

<blockquote>Want direct files? Buy premium and skip verification.</blockquote> 
Check /plan for more info.</b>"""

THIRDT_VERIFY_COMPLETE_TEXT= """<b>Hey {},

You're now verified for today ☺️

Enjoy unlimited movies, series, and anime 💥

Want direct files without verification? Buy our subscription 😁

💶 Check /plan to buy it.</b>"""

VERIFIED_LOG_TEXT = """<b><u>☄ User Verified Successfully ☄</u>

⚡️ Name:- {} [ <code>{}</code> ]
📆 Date:- <code>{}</code></b>

#verification_{}_completed"""

CUSTOM_TEXT = """<b><i>😊 <u>Your group command list</u> 😊

/shortlink - Set shortener
/shortlink2 - Set shortener for 2nd verify
/shortlink3 - Set shortener for 3rd verify
/time2 - Set 2nd verify timing
/time3 - Set 3rd verify timing
/log - Set log channel for user data
/tutorial - Set 1st tutorial video
/tutorial2 - Set 2nd tutorial video
/tutorial3 - Set 3rd tutorial video
/caption - Set custom file caption
/template - Set custom IMDB template
/fsub - Set force subscribe channel
/nofsub - Remove force subscribe
/ginfo - Check group details</i></b>

😘 If you set all this, your group will be awesome..."""

FSUB_TXT = """{},

<i><b>🙁 Please join our channel first to get the file.

Click the join now button below 👇</b></i>"""

DONATE_TXT = """<blockquote>❤️‍🔥 Thanks for your interest in donating</blockquote>

<b><i>💞 If you like this bot, you can donate ₹10, ₹20, ₹50, ₹100, or any amount you wish.</i></b>

❣️ Donations are really helpful to keep this bot running.

💖 UPI ID : <code>Mastertg@postbank</code>"""
