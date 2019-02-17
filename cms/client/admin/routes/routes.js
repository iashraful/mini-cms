import DashboardLayout from "@/admin/pages/Layout/DashboardLayout.vue";

import Dashboard from "@/admin/pages/Dashboard.vue";
import UserProfile from "@/admin/pages/UserProfile.vue";
import TableList from "@/admin/pages/TableList.vue";
import Typography from "@/admin/pages/Typography.vue";
import Icons from "@/admin/pages/Icons.vue";
import Maps from "@/admin/pages/Maps.vue";
import Notifications from "@/admin/pages/Notifications.vue";
import UpgradeToPRO from "@/admin/pages/UpgradeToPRO.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/dashboard",
    children: [
      {
        path: "dashboard",
        name: "Dashboard",
        component: Dashboard
      },
      {
        path: "user",
        name: "User Profile",
        component: UserProfile
      },
      {
        path: "table",
        name: "Table List",
        component: TableList
      },
      {
        path: "typography",
        name: "Typography",
        component: Typography
      },
      {
        path: "icons",
        name: "Icons",
        component: Icons
      },
      {
        path: "maps",
        name: "Maps",
        meta: {
          hideFooter: true
        },
        component: Maps
      },
      {
        path: "notifications",
        name: "Notifications",
        component: Notifications
      },
      {
        path: "upgrade",
        name: "Upgrade to PRO",
        component: UpgradeToPRO
      }
    ]
  }
];

export default routes;
