class Translation(object):
    START_TEXT = """Hello,
This is a Telegram URL Upload Bot for MemeUi_Mirror 😇

<b>Please send me any direct download URL Link, i can upload to telegram as File/Video</b>

/help for more details.. and more thing waiting for u there 😉

Tag @v_m_7_0_3 if any issues"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "Yea Lets Upgrade. But what will u upgrade 🤔"
    FORMAT_SELECTION = "Select the desired format from the buttons given below"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "Downloading 4 U and Wasting My Data 😌"
    UPLOAD_START = "Setting Everything Up For Uploading \nPlease Wait"
    TRIM_START = "Starting Trimming ✂️🎞✂️. Plox Be Patient it's very slow 😁"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2.0GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Happy Now ? 😉🙃😇"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nHappy Now ? 😉🙃 \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "GTFO PLOX. ONLY FOR AUTHORISED USERS"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/ThankTelegram'>@v_m_7_0_3</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "ERROR...🤔 \nPlease provide direct link"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
•••••••••••••••••••••••••••••••
Telegram ID: <code>{}</code>
Plan name: Hyper Peru User
Expires on: 31/12/2069
•••••••••••••••••••••••••••••••"""
    HELP_USER = """Hi iam a Xploader R Bot for @MemeUi_Mirror
    
•••
Use /upload command with link to Upload URL.

•••
You can download youtube videos by giving link. It will automatically download.
Choose the quality u needed as in button

•••
Rename any file and reupload. EXAMPLE :- /rename file_name.extension.

•••
You can unzip any file and download files inside it directly.(Multiple downloads and Folder Download is not possible)

•••
You can generate screenshots of video(file type also) by replying /generatescss to file

•••
For Trimming video
Reply /downloadmedia to the video 
Then use /trim HH:MM:SS HH'MM'SS to trim video
Example - /trim 00:01:00 00:02:00
After these delete the file using /clearmedia so that u can use other media next time.

•••

For Converting Video Files to Streamable Video
Use /c_2_video as reply to the media

•••
COMMON BUTTONS INFO :-

SVideo - Give File as video with Screenshots
DFile  - Give File with Screenshots
Video  - Give File as video without Screenshots
DFile  - Give File without Screenshots

•••
Use /commands for all simple commands list

----------------------------------------------------
Now what are u waiting for 😐🤨
"""
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @xploaderzxbot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Like this plox 👉 /trim HH:MM:SS HH:MM:SS"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "U done wrong boy. Send a compressed (zip,rar) file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists then no hope 😑"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
