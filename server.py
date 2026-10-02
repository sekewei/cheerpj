import http.server
import os
import shutil
import sys
from http import HTTPStatus

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class RangeRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()

        try:
            file_size = os.path.getsize(path)
            file_handle = open(path, "rb")
        except OSError:
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return None

        self.range_start = 0
        self.range_end = file_size - 1
        range_header = self.headers.get("Range")
        if range_header and range_header.startswith("bytes="):
            start_text, _, end_text = range_header[6:].partition("-")
            if start_text:
                self.range_start = int(start_text)
            if end_text:
                self.range_end = int(end_text)
            self.range_end = min(self.range_end, file_size - 1)
            self.send_response(HTTPStatus.PARTIAL_CONTENT)
        else:
            self.send_response(HTTPStatus.OK)

        self.send_header("Content-type", self.guess_type(path))
        self.send_header("Content-Length", self.range_end - self.range_start + 1)
        self.send_header("Content-Range", f"bytes {self.range_start}-{self.range_end}/{file_size}")
        self.send_header("Accept-Ranges", "bytes")
        self.end_headers()
        return file_handle

    def copyfile(self, source, output):
        source.seek(self.range_start)
        remaining = self.range_end - self.range_start + 1
        shutil.copyfileobj(source, output, length=remaining)


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
server = http.server.ThreadingHTTPServer(("127.0.0.1", port), RangeRequestHandler)
print(f"Serving CheerpJ demo at http://localhost:{port}/cheerpj-v3.html")
server.serve_forever()
