package gad.heartbeat.androidflask.easyupload;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

public class Main2Activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

       TextView responseText = (TextView) findViewById(R.id.response1);
        responseText.setText(getIntent().getStringExtra("responsetext"));
     //   Bundle extras = getIntent().getExtras();
     //   byte[] byteArray = extras.getByteArray("image");

      //  Bitmap bmp = BitmapFactory.decodeByteArray(byteArray, 0, byteArray.length);
        ImageView image = (ImageView) findViewById(R.id.imageview);

       // Log.d("image 4","hi");
      //  image.setImageBitmap(bmp);

    }
}
