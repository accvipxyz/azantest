import streamlit as st
import requests
from bs4 import BeautifulSoup
import time
time.sleep(1)

def get_prayer_times(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    prayer_times_table = soup.find('table', class_='ptTable')
    rows = prayer_times_table.find_all('tr')

    prayer_times = {}

    for row in rows[1:]:
        columns = row.find_all('td')
        prayer_name = columns[0].text.strip()
        prayer_time = columns[1].text.strip()
        prayer_times[prayer_name] = prayer_time

    return prayer_times

def main():
    st.title("Prayer Times App")

    url = "https://timesprayer.com/prayer-times-in-sohag.html"

    while True:
        prayer_times = get_prayer_times(url)

        # عرض مواقيت الأذان في واجهة Streamlit
        st.write("### Prayer Times")
        for prayer, time in prayer_times.items():
            st.write(f"{prayer}: {time}")

     
        # انتظر لمدة ثانية قبل تحديث المواقيت
            import time
time.sleep(1)

    

if __name__ == "__main__":
    main()
