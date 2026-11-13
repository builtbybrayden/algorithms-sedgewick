import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URI;
import java.io.IOException;
import java.io.FileWriter;
import java.io.PrintWriter;

public class Wget {

    public static void wget(String url) throws IOException{
        // Find the last slash of the URL where the file name begins, ex. http://example.com/file.csv
        int lastSlash = url.lastIndexOf('/');
        String filename = url.substring(lastSlash + 1);

        // Converts string input to URL for stream to open
        URL site = URI.create(url).toURL();

        // Opening input stream from URL to input, and output to file stream
        try (BufferedReader in = new BufferedReader(new InputStreamReader(site.openStream()));
            PrintWriter out = new PrintWriter(new FileWriter(filename))) {
            
            // Iterates through each line and sends to output stream
            String line = in.readLine();
            while(line != null) {
                out.println(line);
                line = in.readLine();
            }
        }
    }

    public static void main(String[] args) throws IOException {
        wget(args[0]);
    }
}