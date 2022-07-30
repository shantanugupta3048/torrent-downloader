import libtorrent as lt
import time
import sys

source_link = r'magnet:?xt=urn:btih:F4C231734DF63E05D214B08308D2EF93210C1858&dn=The+Lion+King+%282019%29+%5BBluRay%5D+%5B1080p%5D+%5BYTS%5D+%5BYIFY%5D&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.com%3A2710%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce'
source_path = 'Users/kawaiicarrot/Downloads/test.torrent'
out_path = '/Users/kawaiicarrot/Movies/'

ses = lt.session({'listen_interfaces': '0.0.0.0:6881,6882,6883,6884,6885,6886,6887,6888,6889'})

if isinstance(source_link, str):
    params = lt.parse_magnet_uri(source_link)
    params.save_path = out_path
    handle = ses.add_torrent(params)
else:
    params = {'save_path': out_path}
    params['ti'] = lt.torrent_info(source_path)
    handle = ses.add_torrent(params)

begin = time.time()

while not handle.status().has_metadata:
    time.sleep(1)
print('Downloaded Metadata.')

print("Starting", handle.status().name)

while not handle.status().is_seeding:
    s = handle.status()

    state_str = ['Queued', 'Checking', 'Downloading Metadata', 'Downloading', 'Finished', 'Seeding', 'Allocating', 'Checking Fastresume']
    print(
        "\r%.2f%% complete | Down: %.1f mb/s | Up: %.1f mb/s | Peers: %d | %s"
        % (
            s.progress * 100,
            s.download_rate / 1000000,
            s.upload_rate / 1000000,
            s.num_peers,
            state_str[s.state],
        )
    )
    sys.stdout.flush()
    time.sleep(5)

end = time.time()

print(handle.status().name, "Complete")
print('Elasped Time:', int((end-begin)//60), 'min :',int((end-begin)%60), 'sec')