Name:           ros-melodic-geometry2
Version:        0.5.17
Release:        1%{?dist}
Summary:        ROS geometry2 package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/geometry2
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-tf2
Requires:       ros-melodic-tf2-bullet
Requires:       ros-melodic-tf2-eigen
Requires:       ros-melodic-tf2-geometry-msgs
Requires:       ros-melodic-tf2-kdl
Requires:       ros-melodic-tf2-msgs
Requires:       ros-melodic-tf2-py
Requires:       ros-melodic-tf2-ros
Requires:       ros-melodic-tf2-sensor-msgs
Requires:       ros-melodic-tf2-tools
BuildRequires:  ros-melodic-catkin

%description
A metapackage to bring in the default packages second generation Transform
Library in ros, tf2.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Mar 21 2018 Tully Foote <tfoote@osrfoundation.org> - 0.5.17-1
- Autogenerated by Bloom

* Wed Mar 21 2018 Tully Foote <tfoote@osrfoundation.org> - 0.5.17-0
- Autogenerated by Bloom

