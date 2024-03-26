const routes= [
    { path: '/', redirect: '/dashboard' },
    {
      path: '/',
      component: () => import('@/layouts/default.vue'),
      children: [
        {
          path: 'dashboard',
          name: 'dashboard',
          component: () => import('@/pages/dashboard.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'account-settings',
          name: 'account-settings',
          component: () => import('@/pages/account/account-settings.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'data-issues',
          name: 'dataQuality',
          component: () => import('@/pages/data/dataQuality.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'data-sync',
          name: 'dataSync',
          component: () => import('@/pages/data/dataSync.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'users',
          name: 'users',
          component: () => import('@/views/pages/authentication/users.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'system-logs',
          name: 'systemlogs',
          component: () => import('@/views/pages/authentication/system-logs.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'passworddpolicy',
          name: 'passworddpolicy',
          component: () => import('@/views/pages/system_settings/PasswordPolicy.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'dbbackup',
          name: 'dbbackup',
          component: () => import('@/views/pages/system_settings/BackupSchedule.vue'),
          meta: { requiresAuth: true },
        },
      ],
    },
    {
      path: '/',
      component: () => import('@/layouts/blank.vue'),
      children: [
        {
          path: 'login',
          component: () => import('@/pages/account/login.vue'),
        },
        {
          path: 'register',
          component: () => import('@/pages/account/register.vue'),
        },
        {
          path: '/:pathMatch(.)',
          component: () => import('@/pages/[...all].vue'),
        },
      ],
    },
  ]
  
  export default routes
