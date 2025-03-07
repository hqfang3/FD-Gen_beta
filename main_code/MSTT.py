# import library
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from global_parm import *

"Part 1: plotting the fire source locations."
# Parameter - fire source location
# 1 Create the figure to show fire locations
# read the data
def PLOT_FIRE_SOURCE_LOCATIONS(FSL_ID, PARAMETERS_OUTPUT, SKIP_CASE=1):
    
    if isinstance(FSL_ID, list):
        fire_source_location_id=FSL_ID
    else:
        fire_source_location_id=[FSL_ID]
        
    # extract the data from parameter dictionary
    for id in fire_source_location_id:
        for parameter in PARAMETERS_OUTPUT['FSL']:
            if parameter.ID == id:
                # general
                skip_case=SKIP_CASE
                # fire room coordinates
                xL=parameter.XB[0]
                xH=parameter.XB[1]
                yL=parameter.XB[2]
                yH=parameter.XB[3]
                zL=parameter.XB[4]
                zH=parameter.XB[5]
                # burner size
                fire_burner_L=parameter.FIRE_BURNER_SIZE[0]
                fire_burner_W=parameter.FIRE_BURNER_SIZE[1]
                fire_burner_H=parameter.FIRE_BURNER_SIZE[2]
                # mesh size
                mesh_size_x=parameter.MESH_SIZE[0] if parameter.MESH_SIZE[0] is not None else 0.1
                mesh_size_y=parameter.MESH_SIZE[1] if parameter.MESH_SIZE[1] is not None else 0.1
                mesh_size_z=parameter.MESH_SIZE[2] if parameter.MESH_SIZE[2] is not None else 0.1
                # fire source locations
                fire_source_location_x=parameter.SAMPLES[0]
                fire_source_location_y=parameter.SAMPLES[1]
                fire_source_location_z=parameter.SAMPLES[2]
                number_of_samples=len(fire_source_location_x)


                # set the figure
                fig = plt.figure(figsize=(20, 5))
                gs = gridspec.GridSpec(1, 3, width_ratios=[1, 1, 1]) 


                # Create the front view (L x H)
                ax1 = fig.add_subplot(gs[0, 0])
                ax1.set_xlim(xL, xH)
                ax1.set_ylim(zL, zH)
                ax1.set_title('Front View', fontsize=18)
                # Draw a grid
                for i in np.arange(zL, zH + mesh_size_z, mesh_size_z):
                    ax1.axhline(y=i, color='gray', alpha=0.3)
                for j in np.arange(xL, xH + mesh_size_x, mesh_size_x):
                    ax1.axvline(x=j, color='gray', alpha=0.3)
                # Set the limits of the plot
                ax1.set_xticks(np.arange(xL, xH, 1))
                ax1.set_yticks(np.arange(zL, zH, 1))
                ax1.set_xticklabels(ax1.get_xticks(), fontsize=15)
                ax1.set_yticklabels(ax1.get_yticks(), fontsize=15)
                ax1.grid(True, which='both')
                # draw the fire source locations
                for index in range(0, number_of_samples, skip_case):
                    corners = [(fire_source_location_x[index],fire_source_location_z[index]),
                                (fire_source_location_x[index]+fire_burner_L,fire_source_location_z[index]),
                                (fire_source_location_x[index]+fire_burner_L,fire_source_location_z[index]+fire_burner_H),
                                (fire_source_location_x[index],fire_source_location_z[index]+fire_burner_H)]
                    lines = [[corners[0], corners[1]],[corners[1], corners[2]],[corners[2], corners[3]],[corners[3], corners[0]]]
                    for line in lines:
                        plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'b-')
                    x = [corner[0] for corner in corners]
                    y = [corner[1] for corner in corners]
                    plt.fill(x, y, color='red', alpha=0.3)
                    burner_center=[fire_source_location_x[index]+fire_burner_L/2, fire_source_location_z[index]+fire_burner_H/2]
                    plt.scatter(burner_center[0], burner_center[1],color='red', marker='^' )
                    

                # Create the side view (W x H)
                ax2 = fig.add_subplot(gs[0, 1])
                ax2.set_xlim(yL, yH)
                ax2.set_ylim(zL, zH)
                ax2.set_title('Side View', fontsize=18)
                # Draw a grid
                for i in np.arange(zL, zH + mesh_size_z, mesh_size_z):
                    ax2.axhline(y=i, color='gray', alpha=0.3)
                for j in np.arange(yL, yH + mesh_size_y, mesh_size_y):
                    ax2.axvline(x=j, color='gray', alpha=0.3)
                # Set the limits of the plot
                ax2.set_xticks(np.arange(yL, yH, 1))
                ax2.set_yticks(np.arange(zL, zH, 1))
                ax2.set_xticklabels(ax2.get_xticks(), fontsize=15)
                ax2.set_yticklabels(ax2.get_yticks(), fontsize=15)
                ax2.grid(True, which='both')
                # draw the fire source locations
                for index in range(0, number_of_samples, skip_case):
                    corners = [(fire_source_location_y[index],fire_source_location_z[index]),
                                (fire_source_location_y[index]+fire_burner_W,fire_source_location_z[index]),
                                (fire_source_location_y[index]+fire_burner_W,fire_source_location_z[index]+fire_burner_H),
                                (fire_source_location_y[index],fire_source_location_z[index]+fire_burner_H)]
                    lines = [[corners[0], corners[1]],[corners[1], corners[2]],[corners[2], corners[3]],[corners[3], corners[0]]]
                    for line in lines:
                        plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'b-')
                    x = [corner[0] for corner in corners]
                    y = [corner[1] for corner in corners]
                    plt.fill(x, y, color='red', alpha=0.3)
                    burner_center=[fire_source_location_y[index]+fire_burner_W/2, fire_source_location_z[index]+fire_burner_H/2]
                    plt.scatter(burner_center[0], burner_center[1],color='red', marker='^' )
                    
                
                # Create the top view (L x W)
                ax3 = fig.add_subplot(gs[0, 2])
                ax3.set_xlim(xL, xH)
                ax3.set_ylim(yL, yH)
                ax3.set_title('Top View', fontsize=18)
                # Draw a grid
                for i in np.arange(yL, yH + mesh_size_y, mesh_size_y):
                    ax3.axhline(y=i, color='gray', alpha=0.3)
                for j in np.arange(xL, xH + mesh_size_x, mesh_size_x):
                    ax3.axvline(x=j, color='gray', alpha=0.3)
                # Set the limits of the plot
                ax3.set_xticks(np.arange(xL, xH, 1))
                ax3.set_yticks(np.arange(yL, yH, 1))
                ax3.set_xticklabels(ax3.get_xticks(), fontsize=15)
                ax3.set_yticklabels(ax3.get_yticks(), fontsize=15)
                ax3.grid(True, which='both')
                # draw the fire source locations
                for index in range(0, number_of_samples, skip_case):
                    corners = [(fire_source_location_x[index],fire_source_location_y[index]),
                                (fire_source_location_x[index]+fire_burner_L,fire_source_location_y[index]),
                                (fire_source_location_x[index]+fire_burner_L,fire_source_location_y[index]+fire_burner_W),
                                (fire_source_location_x[index],fire_source_location_y[index]+fire_burner_W)]
                    lines = [[corners[0], corners[1]],[corners[1], corners[2]],[corners[2], corners[3]],[corners[3], corners[0]]]
                    for line in lines:
                        plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'b-')
                    x = [corner[0] for corner in corners]
                    y = [corner[1] for corner in corners]
                    plt.fill(x, y, color='red', alpha=0.3)
                    burner_center=[fire_source_location_x[index]+fire_burner_L/2, fire_source_location_y[index]+fire_burner_W/2]
                    plt.scatter(burner_center[0], burner_center[1],color='red', marker='^' )

                # Show the plot
                plt.tight_layout()
                
                plt.savefig(id+".jpg", format='jpg')

    
    return

"Part 2: plotting the HRR curves."
def PLOT_HRR_CURVES(HRC_ID, PARAMETERS_OUTPUT, SKIP_CASE=1):
    
    if isinstance(HRC_ID, list):
        hrr_curve_id=HRC_ID
    else:
        hrr_curve_id=[HRC_ID]
    # extract the data from parameter dictionary
    for id in hrr_curve_id:
        for parameter in PARAMETERS_OUTPUT['HRC']:
            if parameter.ID == id:
                # general
                skip_case=SKIP_CASE
                # hrr curve
                time_slice_samples=parameter.TIME_SLICE_SAMPLES
                hrr_samples=parameter.HRR_SAMPLES
                number_of_samples=len(time_slice_samples)
                
                # set the figure
                fig, ax = plt.subplots(figsize=(20, 10))
                for index in range(0, number_of_samples, skip_case):
                    ax.plot(time_slice_samples[index], hrr_samples[index], alpha=0.7)
                    
                ax.set_xlabel('Time', fontsize=18)
                ax.set_xticks(ax.get_xticks()) 
                ax.set_xticklabels([f"{int(tick)}" for tick in ax.get_xticks()], fontsize=15) 
                ax.set_ylabel('HRR', fontsize=18)
                ax.set_yticks(ax.get_yticks()) 
                ax.set_yticklabels([f"{int(tick)}" for tick in ax.get_yticks()], fontsize=15) 
                plt.savefig(id+".jpg", format='jpg')

            
    return


"Part 3: plotting the generator's distribution."
def PLOT_GENERATOR_SAMPLINGS(PSD_ID, SAMPLE_GENERATOR_OUTPUTS, SKIP_CASE=1):
    
    if isinstance(PSD_ID, list):
        generator_id=PSD_ID
    else:
        generator_id=[PSD_ID]
    # extract the data from parameter dictionary
    for plot_id in generator_id:
        for generator_list in SAMPLE_GENERATOR_OUTPUTS.values():
            for generator in generator_list:
                if plot_id in generator.GENERATOR_ID:
                    # general
                    skip_case=SKIP_CASE
                    # data sample points
                    original_data_samples=generator.SAMPLES[plot_id]
                    data_samples=[]
                    for index in range(0, len(original_data_samples), skip_case):
                        data_samples.append(original_data_samples[index])
            
                    # draw the figure
                    fig, ax = plt.subplots()
                    fig.set_figwidth(20)
                    fig.set_figheight(10)

                    ax.hist(data_samples, bins=10, rwidth=0.8, alpha=0.5)
                    ax.set_ylabel('counts', color='blue', fontsize=18)
                    ax.set_yticks(ax.get_yticks()) 
                    ax.set_yticklabels([f"{round(tick,2)}" for tick in ax.get_yticks()], fontsize=15) 
                    ax1=ax.twinx()
                    sorted_data = np.sort(data_samples)
                    ax1.plot(sorted_data, np.arange(1, len(data_samples) + 1) / len(data_samples), color='red')
                    ax.set_xlabel('data values', fontsize=18)
                    ax.set_xticks(ax.get_xticks())
                    ax.set_xticklabels([f"{round(tick,2)}" for tick in ax.get_xticks()], fontsize=15) 
                    ax1.set_ylabel('cumulative percent', color='red', fontsize=18)
                    ax1.set_yticks(ax1.get_yticks()) 
                    ax1.set_yticklabels([f"{round(tick,2)}" for tick in ax1.get_yticks()], fontsize=15) 
                    title_line1 = 'Random data samples (N={})'.format(len(original_data_samples))
                    title_line2 = 'ID = {}'.format(plot_id)
                    ax.set_title(f'{title_line1}\n{title_line2}', fontsize=18)
                    
                    plt.savefig(plot_id+".jpg", format='jpg')

        
    return