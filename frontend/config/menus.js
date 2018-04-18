import Home from '@/components/Home'
import Login from '@/components/authentications/Login'
import Logout from '@/components/authentications/Logout'
import Settings from '@/components/settings/Settings'
import ProfileSettings from '@/components/settings/ProfileSettings'
import AppConfigSettings from '@/components/settings/AppConfigSettings'
import PageList from '@/components/pages/PageList'
import PageDetails from '@/components/pages/PageDetails'
import UserPageDetails from '@/components/settings/admin/pages/UserPageDetails'
import NotFound from '@/components/utils/common/NotFound'

let menuItems = [
    {
        name: 'Home',
        path: '/',
        identifier: 'app-home',
        component: Home,
        submenus: [],
        dropdown_items: [],
        is_dropdown: false,
        is_hidden: true,
        is_main_menu: true,
        auth: true
    },
    {
        name: 'Settings',
        path: '/settings',
        identifier: 'app-settings',
        component: Settings,
        submenus: [
            {
                name: 'Profile',
                path: 'profile',
                identifier: 'app-settings-profile',
                component: ProfileSettings,
                submenus: [],
                dropdown_items: [],
                is_dropdown: false,
                is_hidden: false,
                is_main_menu: false,
                auth: true
            },
            {
                name: 'Pages',
                path: 'pages',
                identifier: 'app-settings-page-list',
                component: PageList,
                submenus: [],
                dropdown_items: [],
                is_dropdown: false,
                is_hidden: false,
                is_main_menu: false,
                auth: true
            },
            {
                name: 'Page Details',
                path: 'pages/:pageSlug',
                identifier: 'app-settings-page-details',
                component: UserPageDetails,
                submenus: [],
                dropdown_items: [],
                is_dropdown: false,
                is_hidden: true,
                is_main_menu: false,
                auth: true
            },
            {
                name: 'App Config',
                path: 'app-config',
                identifier: 'app-settings-config',
                component: AppConfigSettings,
                submenus: [],
                dropdown_items: [],
                is_dropdown: false,
                is_hidden: true,
                is_main_menu: false,
                auth: true
            }
        ],
        is_dropdown: false,
        is_hidden: true,
        is_main_menu: true,
        auth: true
    },
    {
        name: 'Login',
        path: '/login',
        identifier: 'app-login',
        component: Login,
        submenus: [],
        dropdown_items: [],
        is_dropdown: false,
        is_hidden: true,
        is_main_menu: true,
        auth: false
    },
    {
        name: 'Logout',
        path: '/logout',
        identifier: 'app-logout',
        component: Logout,
        submenus: [],
        is_dropdown: false,
        is_hidden: true,
        is_main_menu: true,
        auth: true
    },
    {
        name: 'NotFound',
        path: '/404',
        identifier: 'app-not-found',
        component: NotFound,
        submenus: [],
        is_dropdown: false,
        is_hidden: true,
        is_main_menu: false,
        auth: false
    },
    {
        name: 'Page Details',
        path: '/p/:pageSlug',
        identifier: 'app-page-details',
        component: PageDetails,
        submenus: [],
        dropdown_items: [],
        is_dropdown: false,
        is_hidden: true,
        is_main_menu: false,
        auth: true
    }
];
export default menuItems;