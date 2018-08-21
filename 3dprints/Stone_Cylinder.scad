//Created by Ari M. Diacou, June 2015
//Shared under Creative Commons License: Attribution 3.0 Unported (CC BY-SA 3.0) 
//see http://creativecommons.org/licenses/by-sa/3.0/

/* [Base] */
//How many blocks form a circle?
blocks_per_rev=12;
//Number of layers of blocks in the turret base
blocks_high=3;
//The height of each block in mm
block_height=4;
//The radial width of a block in mm
block_thickness=10;
//The width of the turret in mm
turret_diameter=60;
//How far the mortar extends from the inside of the blocks in units of block thickness. Range 0-1.
mortar_thickness=.5;
//The type of block being used
stone_type="rough";//["rough","smooth"]
//<1 Compresses layers, >1 expands them to show mortar
z_spacing=1.1;
//<1 Compresses layers, >1 expands them to show mortar
theta_expansion=.95;

/* [Rough Stone Options] */
//A way to save your "random" arrangement
master_seed=1;
//Number of intersections forming a block
n=8;
//reduces the ablity of higher n to cut away all the block, I like -0.4.
power=-.4; //[-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0]
//Maximum angle of block intersections
max_angle=20;

/* [Smooth Stone Options] */
//How much curviness do you want?
$fn=30;
//The radius of curvature of the corners of smooth blocks
curvature=1;

/* [Hidden] */
////////////// Derived Parameters //////////////////////
stone="silver";
grout="ghostwhite";
num=blocks_per_rev;
turret_radius=turret_diameter/2-block_thickness;
rad=turret_radius;           
/////////////////// Main() /////////////////////////////
if(stone_type=="smooth")    
    color(stone) smooth_base();
else
    color(stone) rough_base();
color(grout) mortar(turret_radius,mortar_thickness);
///////////////// Functions ////////////////////////////
module smooth_base(){
	for(h=[0:blocks_high-1]){ //For loop going up
		rotate([0,0,90*(pow(-1,h))/num]) 
			translate([0,0,(h+.5)*block_height*z_spacing]) 
				union(){
					for(i=[1:num]){ //For loop going around
					   rotate( i * 360 / num, [0,0,1])	
							smooth_wedge(turret_radius,block_thickness,360*theta_expansion/num,block_height,curvature);
						}
					}
		}
	}
module rough_base(){
	for(h=[0:blocks_high-1]){
		rotate([0,0,90*(pow(-1,h))/num]) 
			translate([0,0,(h+.5)*block_height*z_spacing]) 
				union(){
					for(i=[1:num]){
					   rotate( i * 360 / num, [0,0,1])	
							scale([1,1,.5]) 
                                rough_wedge(turret_radius,block_thickness,360*theta_expansion/num,block_height,master_seed+i+num*h);
						}
					}
		}
	}    
module mortar(radius,thickness){
	//Makes a filled cylinder in the middle of the bricks of the 
    inner_radius=radius+(1-thickness)*block_thickness/2;
	outer_radius=thickness*block_thickness;
	//translate([0,0,-block_height])
	linear_extrude(blocks_high*block_height*(z_spacing)){
		circle(inner_radius+outer_radius);
		}
	}
module rough_wedge(inner,width,theta,thickness,seed){
	//inner		=inner radius of arch/circle
	//width		=radial distance of block
	//theta		=angle subtended by block
	//thickness	=height of block
	random=rands(-1,1,n*3,seed);
	intersection(){
		wedge_boundary(inner,width,theta,thickness);
		correct(inner, width)	translate([inner+width/2,0,0])
			intersection_for(i=[0:n-1]){
				rotate([	max_angle*random[3*i]*pow(i*(thickness/inner),power),
							.7*max_angle*random[3*i+1]*pow(i,power),
							max_angle*random[3*i+2]*pow(i*(inner/width),power)])
					cube([width, sqrt((4*inner*tan(theta/2))*(width)), sqrt((4*inner*tan(theta/2))*(thickness))], center=true);
				}
		}	
	}
module correct(inner, width){
	//mirrors an object about its yz plane, which necessarily must be done is this ugly way
	translate([inner+width/2,0,0])
		mirror([1,0,0])
			translate([-inner-width/2,0,0])
				children(0);
	}
module wedge_boundary(inner,width,theta,thickness){
	//Creates a pie slice of theta degrees that has a radius of inner+width. Used to make sure that the wedge does not over-extend the angle it is supposed to.
	intersection(){
		rotate([0,0,-theta/2]) 
			translate([(inner+width)/2,(inner+width)/2,0])
				cube([inner+width,inner+width,2*thickness],center=true);
		rotate([0,0,theta/2]) 
			translate([(inner+width)/2,-(inner+width)/2,0])
				cube([inner+width,inner+width,2*thickness],center=true);
		}
	}
module smooth_wedge(inner,width,theta,thickness,curvature){
	//inner		=inner radius of arch
	//width		=width of block
	//theta		=angle subtended by block
	//thickness	=thickness of block
	//curvature	=roundedness of corners, should be less than all of: thickness, width and inner*sin(theta/2)
	//The block is made by a hull around 8 spheres. This function could be created with a minkowski combination of a sphere and a polyhedron, but the rendering time was horrific. It creates a wedge shaped block on the x axis which extends thickness/2 in each of the z-axis directions, and +theta degrees in the xy-plane
	outer=inner+width;
	r=curvature;
	
	
	//     A---------------D     ---
	//      \-------------/      /
	//       \-----------/      } Width
	//        \---------/      /
	//         B-------C --- ---
	//          \theta/  /
    //           \   /  } Inner (radius)
    //            \ /  /
    //             O ---

	//Angles describing the spheres positions must be recalculated so that the objects fit inside the angle called. Positions are translated to cartesian from cylindrical coorinates (r,theta,z). Because the inner spheres B and C subtend more angle, they requrire a different correction angle than outer spheres A and D.
	phi_o=atan(r/(outer-r));
	phi_i=atan(r/(inner+r));

	h=thickness-2*r;
	H=[0,0,h];

	//The principle vectors that define the centers of the spheres
	A=[(outer-r)*cos(theta-phi_o), (outer-r)*sin(theta-phi_o),0]+H/2;
	B=[(inner+r)*cos(theta-phi_i), (inner+r)*sin(theta-phi_i),0]+H/2;
	C=[(inner+r)*cos(phi_i), (inner+r)*sin(phi_i),0]+H/2;
	D=[(outer-r)*cos(phi_o), (outer-r)*sin(phi_o),0]+H/2;

	//The complementary vectors which are below the z axis
	Ac=A-H;
	Bc=B-H;
	Cc=C-H;
	Dc=D-H;
	hull(){
		//The spheres which round the corners, notice the calling of translation vectors above
		translate(A) sphere(r,center=true);
		translate(B) sphere(r,center=true);
		translate(C) sphere(r,center=true);
		translate(D) sphere(r,center=true);
		translate(Ac) sphere(r,center=true);
		translate(Bc) sphere(r,center=true);
		translate(Cc) sphere(r,center=true);
		translate(Dc) sphere(r,center=true);
		}
	}