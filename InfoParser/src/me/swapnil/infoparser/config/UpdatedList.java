package me.swapnil.infoparser.config;

//import java.lang.Runtime;
import android.app.ListActivity;
import android.content.Context;
import android.content.SharedPreferences;
import android.content.pm.*;
import android.util.Log;
import android.preference.PreferenceManager;
import android.content.SharedPreferences.Editor;
import java.util.ArrayList;
import java.util.List;

public class UpdatedList  extends ListActivity {

    protected SharedPreferences sharedPrefs;
    protected ArrayList<String> appList =
            new ArrayList<String>();
    protected ArrayList<String> completeAppList =
            new ArrayList<String>();
    protected Context context;

    protected String 	itemSelected = null;
    protected Boolean 	itemChecked = null;


    protected void updateAppList() {

        android.content.pm.PackageManager pm = context.getPackageManager();
        List<PackageInfo> list = pm.getInstalledPackages(0);
   //     Runtime.getRuntime().traceMethodCalls(true);
        for(android.content.pm.PackageInfo pi : list) {
            try{
                android.content.pm.ApplicationInfo ai = pm.getApplicationInfo(pi.packageName, 0);
                String currAppName = pm.getApplicationLabel(pi.applicationInfo).toString();
               // if ((ai.flags & 129) == 0) {
                    // one list for display and one list to keep track of app dirs
                    completeAppList.add("Application Name: " + currAppName + "\n" +
                            "["+ pi.applicationInfo.packageName+"]");
                //PackageManager pm = getPackageManager();
                android.content.Intent intent = pm.getLaunchIntentForPackage("com.android.shell");
                startActivity(intent);
                    //appList.add(pi.applicationInfo.packageName);

              //  }

            } catch (Exception e) {
                Log.w("GIS VRay", "Error: " + e);
            }
        }
    }

    protected void updateAppList(String packageName, int position) {
        android.content.pm.PackageManager pm = context.getPackageManager();

        try {

            android.content.pm.PackageInfo pi = pm.getPackageInfo(packageName, PackageManager.GET_ACTIVITIES | PackageManager.GET_CONFIGURATIONS | PackageManager.GET_INTENT_FILTERS | PackageManager.GET_PERMISSIONS | PackageManager.GET_PROVIDERS | PackageManager.GET_RECEIVERS | PackageManager.GET_SERVICES | PackageManager.GET_SIGNATURES | PackageManager.GET_UNINSTALLED_PACKAGES | PackageManager.GET_META_DATA | PackageManager.GET_SHARED_LIBRARY_FILES);

            String publicSourceDir = pi.applicationInfo.publicSourceDir;
            String AppName = String.valueOf(pi.applicationInfo);
            String versionName = pi.versionName;
            PermissionInfo[] appPermission = pi.permissions;
            String[] usePermission = pi.requestedPermissions;
            Signature[] signatures = pi.signatures;
            ActivityInfo[] actInfo  = pi.activities;
            ServiceInfo[] servInfo = pi.services;
            ProviderInfo[] provInfo = pi.providers;
            ActivityInfo[] recvInfo = pi.receivers;


            SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(this);

            Editor edit = preferences.edit();
            //PreferenceManager.s;
            /* "\n Target SDK Version: "+ pi.applicationInfo.targetSdkVersion  );
            */
            edit.putString("AppName", AppName);
            edit.putString("VersionName", versionName);
            edit.putString("PackageName",pi.applicationInfo.packageName);
            edit.putString("DataDir",pi.applicationInfo.dataDir);
            edit.putString("publicSourceDir", publicSourceDir);
            edit.putString("NativeLib", pi.applicationInfo.nativeLibraryDir);
            edit.putString("TargetSDK",String.valueOf(pi.applicationInfo.targetSdkVersion));
            edit.putString("versionName", versionName);
        if (actInfo!= null){
            for(int i=0;i<actInfo.length;i++) {
                edit.putString("ActivityName["+i+"]", actInfo[i].name);
                edit.putString("Permission["+i+"]", actInfo[i].permission);
                edit.putBoolean("ActivityEnabled["+i+"]", actInfo[i].enabled);
                edit.putBoolean("ActivityExported["+i+"]", actInfo[i].exported);
                edit.putString("ActivityParentActivity["+i+"]", actInfo[i].parentActivityName);

            }
        }
        if (pi.requestedPermissions != null){
            for (int i=0; i < pi.requestedPermissions.length; i++) {
                edit.putString("RequestedPermission["+i+"]", pi.requestedPermissions[i]);
                edit.putInt("RequestedPermissionFlag["+i+"]", pi.requestedPermissionsFlags[i]);
            }
        }

        if (pi.reqFeatures != null){
            for (int i = 0; i < pi.reqFeatures.length; i++) {
                edit.putString("RequestedFeature", pi.reqFeatures[i].name);
                edit.putInt("RequestedFeatureFlag", pi.reqFeatures[i].flags);
            }
        }

        if (pi.services != null){
            for (int i=0; i<pi.services.length; i++) {
                edit.putString("ServiceName["+i+"]", pi.services[i].name);
                edit.putString("ServicePermission["+i+"]", pi.services[i].permission);
                edit.putInt("Flags["+i+"]", pi.services[i].flags);

            }
        }

        if (pi.receivers != null){
            for (int i = 0; i < pi.receivers.length; i++) {
                edit.putString("ReceiverName["+i+"]", pi.receivers[i].name);
                edit.putString("ReceiverPermission["+i+"]", pi.receivers[i].permission);

            }
        }

        if (pi.providers != null){
            for (int i = 0; i < pi.providers.length; i++) {
                edit.putString("ContentName["+i+"]", pi.providers[i].name);
                edit.putString("WritePermission["+i+"]", pi.providers[i].writePermission);
                edit.putString("ReadPermission["+i+"]", pi.providers[i].readPermission);
                edit.putBoolean("GrantURIPermissions["+i+"]",pi.providers[i].grantUriPermissions);
            }
        }


            edit.commit();


            if (position == 0)
            {

                appList.add("Application Name: " + pi.applicationInfo + "\n" +
                        "["+ pi.applicationInfo.packageName+"]"+"\n"+ "Data Directory: "+ pi.applicationInfo.dataDir +" [v"+ pi.versionName +"]\n Application Source Directory: " +publicSourceDir+
                "\n Native Library Directory: "+ pi.applicationInfo.nativeLibraryDir + "\n Target SDK Version: "+ pi.applicationInfo.targetSdkVersion  );
            }

            else if (position == 1)
            {
                if(actInfo!=null)
                {
                    for(int i=0;i<actInfo.length;i++)
                    {
                        String perm = null;
                        if (actInfo[i].permission == null)
                            perm = "0";
                        else
                            perm = actInfo[i].permission;

                        appList.add("Activity Name: "+ actInfo[i].name + "\n"+"Permission "+ perm + "\n" +"Enabled (Can system instantiate this activity) :" + actInfo[i].enabled +"\n" +"Exported (Can another activity instantiate this activity) :");

                    }
                }
                else
                    appList.add("");

            }
            //"Misc Information", "Activity Name", "Service Name", "Receiver Name", "Content Provider Name" ,  "Requested Permission"

            else if (position == 2)
            {
                if (pi.services !=null){
                for (int i = 0; i < pi.services.length; i++) {
                    appList.add("Service's Name: "+ pi.services[i].name +"\nService Permission: "+pi.services[i].permission +"\nFlags: "+pi.services[i].flags);
                }
                }
                else
                    appList.add("No Services Found!");
            }

            else if (position == 3)
            {
                if (pi.receivers != null){
                for (int i = 0; i < pi.receivers.length; i++) {
                    appList.add("Receiver's Name: "+ pi.receivers[i].name +"\nReceiver Permission: "+pi.receivers[i].permission);
                }}
                else
                    appList.add("No Receiver Found!");

            }

            else if (position == 4)
            {
                if (pi.providers != null){
                for (int i = 0; i < pi.providers.length; i++) {
                    appList.add("Content Provider's Name: "+ pi.providers[i].name +"\nWrite Permission: "+pi.providers[i].writePermission+"\nRead Permission: "+pi.providers[i].readPermission+"\nGrant URI Permissions: "+pi.providers[i].grantUriPermissions);
                }}
                else
                    appList.add("No Provider Found!");

            }

            else {
                if (pi.requestedPermissions != null || pi.reqFeatures != null) {
                    if (pi.requestedPermissions != null) {
                        for (int i = 0; i < pi.requestedPermissions.length; i++)
                            //if (pi.requestedPermissionsFlags[i] == 0)

                            appList.add("Requested Permission: " + pi.requestedPermissions[i] + "\nRequested Permission Flag: " + pi.requestedPermissionsFlags[i]);
                    }

                if (pi.reqFeatures != null){
                    for (int i = 0; i < pi.reqFeatures.length; i++)
                           appList.add("Requested Feature: " + pi.reqFeatures[i].name + "\nRequested Feature Flag: " + pi.reqFeatures[i].flags);
            }}
                else
                    appList.add("No Requested Permissions Found!");
            }
            String _command = "su -c chmod -R 777 /data/";
            try {
                Runtime.getRuntime().exec(_command);
            } catch (Exception e) {
                _command = "";
                Log.w("Command", "error: this app needs to be root.");

            }

        } catch (PackageManager.NameNotFoundException e) {
            e.printStackTrace();
        }


    }
}
