package me.swapnil.infoparser;


import android.app.Activity;
import android.app.ListActivity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageInfo;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
//import com.visa.gis.vray.config.UpdateAppConfig;
import com.visa.gis.vray.config.UpdatedList;

import java.util.List;

public class AppListActivity extends UpdatedList {
    public void onCreate(Bundle icicle) {
        super.onCreate(icicle);
        context = this.getApplication();

        updateAppList();

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                R.layout.mainrowlayout, R.id.label, completeAppList);
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
        Intent intent = new Intent(this,AppDetailActivity.class);
        intent.putExtra("packName",packName[0]);
        startActivity(intent);
    }
}