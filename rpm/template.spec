Name:           ros-kinetic-bin-pose-emulator
Version:        0.1.4
Release:        0%{?dist}
Summary:        ROS bin_pose_emulator package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-bin-pose-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-visualization-msgs
Requires:       yaml-cpp-devel
BuildRequires:  ros-kinetic-bin-pose-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  yaml-cpp-devel

%description
bin_pose_emulator generates random poses of items in the predefined bin.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Sep 08 2017 Frantisek Durovsky <durovsky@photoneo.com> - 0.1.4-0
- Autogenerated by Bloom

* Thu Jul 06 2017 Frantisek Durovsky <durovsky@photoneo.com> - 0.1.3-0
- Autogenerated by Bloom

* Mon Jun 12 2017 Frantisek Durovsky <durovsky@photoneo.com> - 0.1.2-0
- Autogenerated by Bloom

* Tue Jun 06 2017 Frantisek Durovsky <durovsky@photoneo.com> - 0.1.1-0
- Autogenerated by Bloom

