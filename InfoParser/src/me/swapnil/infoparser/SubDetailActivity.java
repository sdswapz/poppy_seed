package me.swapnil.infoparser;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

/**
 * Created by msp on 3/28/14.
 */
public class SubDetailActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sub_detail);
        TextView view = (TextView)findViewById(R.id.info);
        String extraInfo = getIntent().getStringExtra("ITEM_SELECTED");
        setTitle(extraInfo);
        extraInfo = "Android has security features built into the operating system that significantly reduce the frequency and impact of application security issues. The system is designed so you can typically build your apps with default system and file permissions and avoid difficult decisions about security";

        Log.e("SubDetailActivity",extraInfo);
        view.setText(extraInfo);
    }

}
