package me.swapnil.infoparser;


import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import com.visa.gis.vray.config.UpdatedList;

//import com.visa.gis.vray.config.UpdateAppConfig;

public class MoreDetailedActivity extends UpdatedList {
    public void onCreate(Bundle icicle) {
        super.onCreate(icicle);
        context = this.getApplication();
        Intent intent =  getIntent();
        String position = intent.getStringExtra("ItemSel");
        String packName = intent.getStringExtra("PackName");


        updateAppList(packName, Integer.parseInt(position));

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                R.layout.activity_sub_details, R.id.label, appList);
        setListAdapter(adapter);
    }

    @Override
    public void onListItemClick(ListView l, View v, int position, long id) {
        String item = (String) getListAdapter().getItem(position);
        item.trim();
        String [] packN = item.trim().split("\\[");
        String [] packName = packN[1].trim().split("\\]");
        Log.e("TEST selected ",packName[0]);
//        Toast.makeText(this, item + " selected", Toast.LENGTH_LONG).show();
        Intent intent = new Intent(this,SubDetailActivity.class);
        intent.putExtra("packName",packName[0]);
        startActivity(intent);
    }
}